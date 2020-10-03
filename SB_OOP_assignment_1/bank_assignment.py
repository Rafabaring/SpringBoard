import json
from dbutils import get_id

class Customer:
    """
    description: Initiate a new customer in the bank
                 In here, the customer can withdraw, deposit and transfer money

    parameter: first_name, last_name

    return: instance of Customer
    """
    def __init__(self, first_name, last_name):
        id = get_id("customer")
        customer_payload = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name
        }

        self.id = id
        self.first_name = first_name
        self.last_name  = last_name
        self.payload = customer_payload


    def _test_fund_available(self, current_amount, withdraw_amount):
        if withdraw_amount > current_amount:
            raise ValueError("Not enought funds to withdraw")


    def _test_account_available(self, mirror_database):
        if len(mirror_database["account"]) == 0:
            raise ValueError("You need an account to perform deposit of withdraw operations")


    def account_operation(self, operation_type, amount, payload_to_operate):
        if operation_type == "withdraw":
            self._test_fund_available(payload_to_operate["balance"], amount)
            payload_to_operate["balance"]  -= amount
        elif operation_type == "deposit":
            payload_to_operate["balance"]  += amount
        return payload_to_operate


    # A transfer is just a simple combination of withdrawing and adding funds to different accounts
    def transfer(self, recipient, amount):
        self.withdraw(amount)
        recipient.deposit(amount)





class Account:
    """
    description: Initiate a new account given a Customer and a Employee/Manager
                 Balance has a default parameter = 0, but can be changed with the Customer methods

    parameter: instance of Customer, instance of Employee, account_type, balance = 0

    return: instance of Account
    """
    def __init__(self, Customer, Employee, account_type, balance = 0):
        id = get_id("account")
        account_payload = {
        "id": id,
        "customer_id": Customer.id,
        "manager_id": Employee.id,
        "account_type": account_type,
        "balance": balance
        }

        self.id = id
        self.id_customer = Customer.id
        self.id_employee = Employee.id
        self.account_type = account_type
        self.balance = balance
        self.payload = account_payload





class Employee:
    """
    description: Initiate an Employee, that will server as a Manager when opening an acccount

    parameter: first_name, last_name, branch, role

    return: instance of Employee
    """
    def __init__(self, first_name, last_name, branch, role):
        id = get_id("employee")
        employee_payload = {
        "id": id,
        "first_name": first_name,
        "last_name":  last_name,
        "branch":     branch,
        "role":       role
        }

        self.id  = id
        self.first_name = first_name
        self.last_name = last_name
        self.branch = branch
        self.role = role
        self.payload = employee_payload





class Service:
    """
    description: User can register for loans in this class

    parameter: service_type, Customer

    return: instance of Service
    """
    def __init__(self, service_type, Customer):
        id = get_id("service")
        service_payload = {
        "id": id,
        "customer_id": Customer.id,
        "service_type": service_type
        }

        self.id  = id
        self.id_customer = Customer.id
        self.service_type = service_type # credit card or loan
        self.payload = service_payload



    def request_loan(self, Customer, amount, payload_to_operate):
        return Customer.account_operation("deposit", amount, payload_to_operate)
