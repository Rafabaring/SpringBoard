import psycopg2
import sqlManager
import config as cfg


hostname = cfg.HOSTNAME
username = cfg.USERNAME
password = cfg.PASSWORD
database = cfg.DATABASE


postgree_connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

# Create table
sqlManager.createTable("sales", postgree_connection)

# Importing the CSV file
path_to_file = "/path/to/raw/data.csv"
sqlManager.insertCSVIntoTable(postgree_connection, "sales", path_to_file)

# Getting most popular results
results = sqlManager.get_most_popular(postgree_connection, "event_name", "sales")

# Closing connection
postgree_connection.close()
