from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from pyspark.sql import SQLContext
from pyspark.sql.functions import col, max as max_

import load_data
rdd_join = load_data.rdd_join
sqlContext = SQLContext(load_data.sc)
schema = StructType([
    StructField("trade_dt",StringType(),True),
    StructField("rec_type",StringType(),True),
    StructField("symbol",StringType(),True),
    StructField("exchange", StringType(), True),
    StructField("event_tm", StringType(), True),
    StructField("event_seq_nb", StringType(), True),
    StructField("arrival_tm", StringType(), True),
    StructField("trade_pr", StringType(), True),
    StructField("bid_pr", StringType(), True),
    StructField("bid_size", StringType(), True),
    StructField("ask_pr", StringType(), True),
    StructField("ask_size", StringType(), True),
    StructField("execution_id", StringType(), True),
    StructField("trade_size", StringType(), True)
  ])

 # Creating a dataframe for all data
common_df = sqlContext.createDataFrame(rdd_join, schema)

# Working with TRADES data:
trade = common_df.filter(common_df.rec_type == "T")

# Selecting most important columns to save space
trade_df = trade.select('trade_dt',
                         'symbol',
                         'exchange',
                         'event_tm',
                         'event_seq_nb',
                         'trade_pr',
                         'execution_id',
                         'trade_size',
                         'arrival_tm')

# Grouping by to get the latest value
trade_gb = trade_df.withColumn("arrival_tm", col("arrival_tm").cast("timestamp")
        ).groupBy('trade_dt',
                  'symbol',
                  'exchange',
                  'event_tm',
                  'event_seq_nb').agg(max_('arrival_tm'))


# Joining the data with the latest arrival_tm to get the rest of the columns
trade_complete = trade_gb.join(trade, ['trade_dt',
                                       'symbol',
                                       'exchange',
                                       'event_tm',
                                       'event_seq_nb'], how = 'left')

# Working with QUOTES data:
quotes = common_df.filter(common_df.rec_type == "Q")

# Selecting most important columns to save space
quotes_df = quotes.select('trade_dt',
                         'symbol',
                         'exchange',
                         'event_tm',
                         'event_seq_nb',
                         'trade_pr',
                         'execution_id',
                         'trade_size',
                         'arrival_tm')

# Grouping by to get the latest value
quotes_gb = quotes_df.withColumn("arrival_tm", col("arrival_tm").cast("timestamp")
        ).groupBy('trade_dt',
                  'symbol',
                  'exchange',
                  'event_tm',
                  'event_seq_nb').agg(max_('arrival_tm'))


# Joining the data with the latest arrival_tm to get the rest of the columns
quotes_complete = quotes_gb.join(quotes, ['trade_dt',
                                       'symbol',
                                       'exchange',
                                       'event_tm',
                                       'event_seq_nb'], how = 'left')

# Concatenating trades and quotes
trades_and_quotes_last_df = trade_complete.union(quotes_complete)
trades_and_quotes_last_df = trades_and_quotes_last_df.select('trade_dt',
                                                              'rec_type',
                                                              'symbol',
                                                              'exchange',
                                                              'event_tm',
                                                              'event_seq_nb',
                                                              'arrival_tm',
                                                              'trade_pr',
                                                              'bid_pr',
                                                              'bid_size',
                                                              'ask_pr',
                                                              'ask_size',
                                                              'execution_id',
                                                              'trade_size')

# Converting back to RDD to perform DB and logging operations
trade_complete_rdd = trade_complete.rdd.map(tuple)
quotes_complete_rdd = quotes_complete.rdd.map(tuple)
trades_and_quotes_last_rdd = trades_and_quotes_last_df.rdd.map(tuple)

# Logging file
import log_manager as log
log.log_daily_records(trade_complete_rdd.collect(), "last_update_trade")
log.log_daily_records(quotes_complete_rdd.collect(), "last_update_quote")
log.log_daily_records(trades_and_quotes_last_rdd.collect(), "last_update_trades_quote")


# Pushing last up to date data to database
from sqlManager import *

# Initiate the database
db = Database()
postgree_connection = db.connect()

# Create Postgree table if still doesn't exist
# db.createTable(postgree_connection, "events")

# Inserting raw data into events table:
db.insertRddIntoTable(postgree_connection, trades_and_quotes_last_rdd.collect(), "events")
