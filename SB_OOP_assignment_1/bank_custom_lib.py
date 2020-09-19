import json

def initiate_database():
    """
    Initializing a txt file that will serve as database for this practice
    In it will be created a json representing all data from 4 different tables:
    customer, account, employee and service
    """
    try:
        with open('database.txt', 'w+') as database:
            database_data = {}
            database_data['customer'] = []
            database_data['account'] = []
            database_data['employee'] = []
            database_data['service'] = []
            json.dump(database_data, database)
            database.close()
    except IOError:
        print('file not found')





def insert_into_database(table_name, payload):
    """
    Append to the list simulating the effect of adding a new row to a table
    """
    with open('database.txt', 'r+') as database:
        database_data = json.load(database)
        database_data[table_name].append(payload)
        database.seek(0)
        json.dump(database_data, database)
        database.close()


def get_id(table_name):
    """
    Return the id based on the lenght of the current table
    The new id will be the last index of a list
    """
    with open('database.txt', 'r+') as database:
        database_data = json.load(database)
        last_index = len(database_data[table_name])
        database.close()
        return last_index
