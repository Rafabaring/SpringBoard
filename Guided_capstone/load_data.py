from pyspark import SparkConf, SparkContext

# Starting the spark context
conf = SparkConf().setMaster("local").setAppName("parse_data")
sc = SparkContext(conf = conf)

# path_to_csv = 's3://trades-quotes-capstone/data/csv/2020-08-05/NYSE/part-00000-5e4ced0a-66e2-442a-b020-347d0df4df8f-c000.txt'
# Local path used for local testing
csv_lines = sc.textFile(path_to_csv)

# Defining the CSV parser
import data_parse_helper as dp
rdd_csv = csv_lines.map(dp.parse_csv)#.collect()


# path_to_json = 's3://trades-quotes-capstone/data/json/2020-08-05/NASDAQ/part-00000-c6c48831-3d45-4887-ba5f-82060885fc6c-c000.txt'
# Local path used for local testing
json_lines = sc.textFile(path_to_json)

# Defining the json parser
rdd_json = json_lines.map(dp.parse_json)#.collect()


# Joining rdd from CSV data and JSON data
rdd_join = rdd_csv.union(rdd_json)
rdd_combined = rdd_join.collect()


# Sending data to Postgre Database
import psycopg2
import sqlManager
import config as cfg

hostname = cfg.HOSTNAME
username = cfg.USERNAME
password = cfg.PASSWORD
database = cfg.DATABASE


postgree_connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

# Create Postgree table if still doesn't exist
sqlManager.createTable(postgree_connection, "raw_events")

# Inserting raw data into raw_events table:
sqlManager.insertRddIntoTable(postgree_connection, rdd_combined,"raw_events")

# Logging file
import log_daily_raw_events
current_date = log_daily_raw_events.current_date
log_daily_raw_events.log_daily_records(rdd_combined, "raw")
log_daily_raw_events.log_daily_records_s3(
        '/Users/rafaelbaring/Documents/SpringBoard/Guided_capstone/daily_log/daily_log_' + current_date + ".txt",
        'trades-quotes-capstone',
        'daily_log_' + current_date + '.txt'
        )
