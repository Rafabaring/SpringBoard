import json
from bank_assignment import *
from bank_custom_lib import update_database, initiate_database, get_id, update_partial_database


def is_client_satisfied():
    """
    description: Called at the beggining of the "main" function. It verifies if the client
                 wants any other service or if they are happy. If they are happy, ends the program

    parameter: None

    return: final_answer --> client satisfaction
    """
    print("\nIs that all?\n")
    final_answer = input("y / n: ")
    return final_answer





def register_customer_console(mirror_database):
    """
    description: Creates an instance of the Customer class

    parameter: mirror_database

    return: updated mirror_database and an instance of Customer class
    """
    print("Please input your first Name\n")
    first_name = input()
    print("And now your last name\n")
    last_name = input()

    new_customer = Customer(first_name, last_name)
    mirror_database = update_partial_database("customer", new_customer.payload, mirror_database)

    print("The bank welcomes you as a new client\n")
    return new_customer, mirror_database





def create_account_console(new_customer, employee, mirror_database):
    """
    description: Creates an instance of the Account class

    parameter: mirror_database

    return: updated mirror_database and an instance of Account class
    """
    print("What type of account would you like to create? Checking or Savings\n")
    account_type = input().lower()

    new_account = Account(new_customer, employee, account_type)
    mirror_database = update_partial_database('account', new_account.payload, mirror_database)


    print("Congratulations, your account was created successfully\n")
    return mirror_database





def account_operation_console(new_customer, mirror_database):
    """
    description: performs an operation (deposit or withdraw) using methods from Customer class

    parameter: mirror_database and instance of Customer class

    return: updated mirror_database
    """
    print("Awesome! What operation would you like to do? Deposit or Withdraw\n")
    operation_type = input().lower()

    print("Great choice! And which account would you like to operate? Checking or Savings\n")
    account_type = input().lower()

    print("How much would you like to deposit or withdraw\n")
    amount = int(input())

    # Executing the operation
    mirror_database = new_customer.account_operation(operation_type, account_type, amount, mirror_database)

    print("Hooray, your operation was performed beautifully\n")
    return mirror_database





def service_or_loan_console(new_customer, mirror_database):
    """
    description: Creates an instance of the Service class and, if requested, utilizes the request_loan method from Services class

    parameter: mirror_database and instance of Customer class

    return: updated mirror_database
    """
    print("We offer credit-card or loan as services. Which one would you like?\n")
    service_type = input().lower()
    new_service = Service(service_type, new_customer)
    mirror_database = update_partial_database("service", new_service.payload, mirror_database)

    print("Awesome, all set up\n")

    # Case the service is a loan, we offer to request a loan (meaning borrow the money)
    if service_type == "loan":
        print("Given you created a loan, would you like to request it?\n")
        loan_y_n = input("y / n: ")
        if loan_y_n == "y":
            print("Awesome!, how much would you like to request?\n")
            loan_amount = int(input())
            mirror_database = new_service.request_loan(new_customer, loan_amount, mirror_database)
        else:
            print("Cool! No worries :)")
    return mirror_database
