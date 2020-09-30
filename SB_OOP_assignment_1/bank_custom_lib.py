import json

def initiate_database():
    """
    Initializing a txt file that will serve as database for this practice
    In it will be created a json representing all data from 4 different tables:
    customer, account, employee and service
    """
    try:
        with open("database.txt", "w+") as database:
            database_data = {}
            database_data["customer"] = []
            database_data["account"] = []
            database_data["employee"] = []
            database_data["service"] = []
            json.dump(database_data, database)
            database.close()
    except IOError:
        print("file not found")





def update_partial_database(table_name, payload, outstanding_database):
    outstanding_database[table_name].append(payload)
    return outstanding_database





def update_database(mirror_database):
    """
    Append to the list simulating the effect of adding a new row to a table
    """
    with open("database.txt", "r+") as database:
        database.seek(0)
        json.dump(mirror_database, database)
        database.close()





def get_id(table_name):
    """
    Return the id based on the lenght of the current table
    The new id will be the last index of a list
    """
    with open("database.txt", "r+") as database:
        database_data = json.load(database)
        last_index = len(database_data[table_name])
        database.close()
        return last_index
