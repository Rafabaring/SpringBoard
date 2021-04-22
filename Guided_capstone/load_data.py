from pyspark import SparkConf, SparkContext
import config as cfg

# Starting the spark context
conf = SparkConf().setMaster("local").setAppName("parse_data")
sc = SparkContext(conf = conf)

# path_to_csv = cfg.s3_path_to_csv
# Local path used for local testing
path_to_csv = cfg.local_path_to_csv
csv_lines = sc.textFile(path_to_csv)

# Defining the CSV parser
import data_parse_helper as dp
rdd_csv = csv_lines.map(dp.parse_csv)


# path_to_json = cfg.s3_path_to_json
# Local path used for local testing
path_to_json = cfg.local_path_to_json
json_lines = sc.textFile(path_to_json)

# Defining the json parser
rdd_json = json_lines.map(dp.parse_json)


# Joining rdd from CSV data and JSON data
rdd_join = rdd_csv.union(rdd_json)
rdd_combined = rdd_join.collect()


# Sending data to Postgre Database
from sqlManager import *

# Initiate the database
db = Database()
postgree_connection = db.connect()

# Create Postgree table if still doesn't exist
# db.createTable(postgree_connection, "raw_events")

# Inserting raw data into raw_events table:
db.insertRddIntoTable(postgree_connection, rdd_combined,"raw_events")

# Logging file
import log_manager as log
current_date = log.current_date
# Logging to local directory
log.log_daily_records(rdd_combined, "raw")

# Loggint to cloud storage
log.log_daily_records_s3(
        cfg.local_log_path + current_date + ".txt",
        'trades-quotes-capstone',
        'daily_log_' + current_date + '.txt'
        )
