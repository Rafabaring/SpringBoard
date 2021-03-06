import psycopg2
import pandas as pd

def createTable(table_name, conn):
    cur = conn.cursor()
    create_table_query = "CREATE TABLE " +  table_name + ''' (
                            ticket_id INT,
                            trans_date DATE,
                            event_id INT,
                        	event_name VARCHAR(150),
                        	event_date DATE,
                        	event_type VARCHAR(100),
                        	event_city VARCHAR(100),
                        	customer_id INT,
                        	price DECIMAL,
                        	num_tickets INT
                        )'''
    cur.execute(create_table_query)
    conn.commit() # save changes in database
    print("Table created")



def insertIntoTable(conn, row_to_input, table):
    '''
    row_to_input should be a tuple following this format:
    (1, '2020-08-01', 100, 'The North American International Auto Show', '2020-09-01', 'Exhibition', 'Michigan', 123, 35.0, 3)
    (2, '2020-08-03', 101, 'Carlisle Ford Nationals', '2020-09-30', 'Exhibition', 'Carlisle', 151, 43.0, 1)
    (3, '2020-08-03', 102, 'Washington Spirits vs Sky Blue FC', '2020-08-30', 'Sports', 'Washington DC', 223, 59.34, 5)
    ...
    '''
    cur = conn.cursor()
    insert_value_query = "INSERT INTO " + table + " VALUES " + str(row_to_input)
    cur.execute(insert_value_query)
    conn.commit() # save changes in database


def insertCSVIntoTable(conn, table, file):
    # Importing the file
    raw_data = pd.read_csv(file, header=None)

    # Adding a header to the dataframde for a better visualization
    raw_data.columns = (['ticket_id',
                         'trans_date',
                         'event_id',
                         'event_name',
                         'event_date',
                         'event_type',
                         'event_city',
                         'customer_id',
                         'price',
                         'num_tickets'])

    # Creating the tuple to be inserted in the database
    for row_number in range (0, len(raw_data)):
        row_to_input = (
            raw_data['ticket_id'][row_number],
            raw_data['trans_date'][row_number],
            raw_data['event_id'][row_number],
            raw_data['event_name'][row_number],
            raw_data['event_date'][row_number],
            raw_data['event_type'][row_number],
            raw_data['event_city'][row_number],
            raw_data['customer_id'][row_number],
            raw_data['price'][row_number],
            raw_data['num_tickets'][row_number]
        )
        insertIntoTable(conn, row_to_input, table)
    print("CSV file imported successfully")


def get_most_popular(conn, field, table):
    cur = conn.cursor()
    get_most_popular_query = "SELECT " + field + ", COUNT(ticket_id) ticket_count FROM " + table + " GROUP BY " + field + " ORDER BY COUNT(ticket_id) DESC"
    cur.execute(get_most_popular_query)
    results = cur.fetchall()
    print("Here are the most popular events")
    print(results)
    return results
