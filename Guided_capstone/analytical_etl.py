from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

import EOD_job as eod_job
import load_data as ld

import log_manager as log

spark = SparkSession.builder.appName("analytical_etl").getOrCreate()

# Creating temporary views
eod_job.common_df.createOrReplaceTempView("tmp_trade_moving_avg")
eod_job.common_df.createOrReplaceTempView("tmp_last_trade")
eod_job.common_df.createOrReplaceTempView("tmp_quotes")

# Querying moving average data
mvg_avg = spark.sql("""
    SELECT
        trade_dt,
        symbol,
        exchange,
        event_tm,
        event_seq_nb,
        trade_pr,
        mean(trade_pr)
     OVER
         (PARTITION BY symbol, exchange ORDER BY event_tm RANGE BETWEEN INTERVAL 30 MINUTES PRECEDING AND CURRENT ROW) AS mov_avg_pr
    FROM
        tmp_trade_moving_avg
            """)


# Logging results
log.log_daily_records(mvg_avg, "mvg_avg")

# Querying last trade price
last_trade_pr = spark.sql("""
    SELECT
        trade_dt,
        symbol,
        exchange,
        trade_pr as last_td_pr
    FROM
     (
        SELECT
            trade_dt,
            symbol,
            exchange,
            event_tm,
            event_seq_nb,
            trade_pr,
            ROW_NUMBE() OVER(PARTITION BY symbol, exchange ORDER BY event_tm DESC, event_seq_nb DESC) as r_number
        FROM
            tmp_last_trade
    ) a
    WHERE
        r_number = 1
            """)

# Logging results
log.log_daily_records(last_trade_pr, "last_trade_pr")



# Querying quote_union
last_trade_pr = spark.sql("""
    SELECT
        trade_dt,
        symbol,
        exchange,
        event_tm,
        event_seq_nb,
        bid_pr,
        bid_size,
        ask_pr,
        ask_size
    FROM
        quotes
    UNION ALL
    SELECT
        trade_dt,
        symbol,
        exchange,
        event_tm,
        event_seq_nb,
        bid_pr,
        bid_size,
        ask_pr,
        mov_avg_pr
    FROM
        tmp_trade_moving_avg
            """)

# Logging results
log.log_daily_records(last_trade_pr, "last_trade_pr")
