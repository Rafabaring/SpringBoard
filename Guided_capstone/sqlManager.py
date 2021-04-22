import psycopg2
import pandas as pd
import config as cfg


class Database:
    def __init__(self):
        self.hostname = cfg.HOSTNAME
        self.username = cfg.USERNAME
        self.password = cfg.PASSWORD
        self.database = cfg.DATABASE




    def connect(self):
        postgree_connection = psycopg2.connect(host=self.hostname,
                                               user=self.username,
                                               password=self.password,
                                               dbname=self.database)

        return postgree_connection




    def createTable(self, conn, table_name):
        cur = conn.cursor()
        create_table_query = "CREATE TABLE " +  table_name + ''' (
                                trade_dt     VARCHAR(150),
                                rec_type     VARCHAR(150),
                                symbol       VARCHAR(150),
                                exchange     VARCHAR(150),
                                event_tm     VARCHAR(150),
                                event_seq_nb VARCHAR(150),
                                arrival_tm   VARCHAR(150),
                                trade_pr     VARCHAR(150),
                                bid_pr       VARCHAR(150),
                                bid_size     VARCHAR(150),
                                ask_pr       VARCHAR(150),
                                ask_size     VARCHAR(150),
                                execution_id VARCHAR(150),
                                trade_size   VARCHAR(150)
                            )'''
        if table_name == 'events':
            create_table_query = create_table_query.replace('arrival_tm   VARCHAR(150)', 'arrival_tm   TIMESTAMP')

        cur.execute(create_table_query)
        conn.commit() # save changes in database
        print("Table created")





    def insertRddIntoTable(self, conn, rdd_to_input, table):
        cur = conn.cursor()
        for row in rdd_to_input:
            insert_value_query = "INSERT INTO " + table + " VALUES " + str(row)
            cur.execute(insert_value_query)
        conn.commit() # save changes in database
