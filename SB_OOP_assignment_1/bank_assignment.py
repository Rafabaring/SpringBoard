import json
from bank_custom_lib import insert_into_database, initiate_database, get_id

# Initiate the database: More details on how this is done can be found in "bank_custom_lib.py" docstring
initiate_database()

class Customer:
    """
    Initiate a new customer in the bank
    In here, the customer can withdraw, deposit and transfer money
    """
    def __init__(self, first_name, last_name):
        id = get_id('customer')
        customer_payload = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name
        }
        insert_into_database('customer', customer_payload)

        self.id = id
        self.first_name = first_name
        self.last_name  = last_name

    # Client has the hability to withdraw from his balance
    def withdraw(self, amount):
        def test_funds_available(current_amount, withdraw_amount):
            if withdraw_amount > current_amount:
                raise ValueError("Not enought funds to withdraw")

        with open('database.txt', 'r+') as database:
            database_data = json.load(database)
            # [account['balance']  -= amount for account in database_data['account'] if (account['customer_id'] == self.first_name)]
            # Try to use list comprehension
            for account in database_data['account']:
                if account['customer_id'] == self.id:
                    test_funds_available(account['balance'], amount)
                    account['balance']  -= amount
            database.seek(0)
            json.dump(database_data, database)
            database.close()

    # Client has the hability to add more funds to his balance
    def deposit(self, amount):
        with open('database.txt', 'r+') as database:
            database_data = json.load(database)

            for account in database_data['account']:
                if account['customer_id'] == self.id:
                    account['balance']  += amount
            database.seek(0)
            json.dump(database_data, database)
            database.close()

    # A transfer is just a simple combination of withdrawing and adding funds to different accounts
    def transfer(self, recipient, amount):
        self.withdraw(amount)
        recipient.deposit(amount)





class Account:
    """
    Initiate a new account given a Customer and a Employee/Manager
    Balance has a default parameter = 0, but can be changed with the Customer methods
    """
    def __init__(self, Customer, Employee, account_type, balance = 0):
        id = get_id('account')
        account_payload = {
        "id": id,
        "customer_id": Customer.id, # Trocar por ID antes de subir
        "manager_id": Employee.id, # Trocar por ID antes de subir
        "account_type": account_type,
        "balance": balance
        }
        insert_into_database('account', account_payload)

        self.id = id
        self.id_customer = Customer.id
        self.id_employee = Employee.id
        self.account_type = account_type
        self.balance = balance





class Employee:
    """
    Initiate an Employee, that will server as a Manager when opening an acccount
    """
    def __init__(self, first_name, last_name, branch, role):
        id = get_id('employee')
        employee_payload = {
        "id": id,
        "first_name": first_name,
        "last_name":  last_name,
        "branch":     branch,
        "role":       role
        }
        insert_into_database('employee', employee_payload)

        self.id  = id
        self.first_name = first_name
        self.last_name = last_name
        self.branch = branch
        self.role = role





class Service:
    """
    User can register for loans in this class
    """
    def __init__(self, service_type, Customer):
        id = get_id('service')
        service_payload = {
        "id": id,
        "customer_id": Customer.id,
        "service_type": service_type
        }
        insert_into_database('service', service_payload)

        self.id  = id
        self.id_customer = Customer.id
        self.service_type = service_type # credit card or loan

    # The loan should work just in case the service_type is a loan
    def request_loan(self, Customer, amount, service_type = 'loan'):
        if service_type != 'loan':
            raise ValueError("Service only available for loans")
        else:
            Customer.deposit(amount)
            print("Approved")
