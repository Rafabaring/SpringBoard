import json


class OutstandingDatabase:
    def __init__(self):
        """
        Initializing a txt file that will serve as database for this practice
        In it will be created a json representing all data from 4 different tables:
        customer, account, employee and service
        """
        try:
            with open("database.txt", "w+") as database:
                database_data = {}
                database_data["customer"] = [{"id": 0, "first_name": "Rafael", "last_name": "Baring"}] # initiate the database with some data in it
                database_data["account"] = []
                database_data["employee"] = []
                database_data["service"] = []
                json.dump(database_data, database)
                database.close()
        except IOError:
            print("file not found")

        self.data = database_data





    def update_partial_database(self, table_name, payload):
        # Initially check if the payload exists in the table already
        table_id_list = [id['id'] for id in self.data[table_name]]
        if payload['id'] in table_id_list:
            self.data[table_name][payload['id']] = payload
        else:
            self.data[table_name].append(payload)





    def verify_existing_user(self, first_name, last_name):
        for customer in self.data["customer"]:
            if customer["first_name"] == first_name and customer["last_name"] == last_name:
                customer_verified = True
            else:
                customer_verified = False
        return customer_verified






    def get_client_to_operate(self,id, account_to_operate):
        for account in self.data['account']:
            if account['customer_id'] == id and account["account_type"] == account_to_operate:
                return account
            else:
                print("No account related")
                return None





    def update_database(self):
        """
        Append to the list simulating the effect of adding a new row to a table
        """
        with open("database.txt", "r+") as database:
            database.seek(0)
            json.dump(self.data, database)
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
