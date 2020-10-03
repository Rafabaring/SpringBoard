import json
from bank_assignment import *
from dbutils import *


def is_client_satisfied():
    """
    description: Called at the beggining of the "main" function. It verifies if the client
                 wants any other service or if they are happy. If they are happy, ends the program

    parameter: None

    return: final_answer --> client satisfaction
    """
    print("\nIs that all?\n")
    final_answer = input_validation('y_n')

    return final_answer





def register_customer_console():
    """
    description: Creates an instance of the Customer class

    parameter: mirror_database

    return: updated mirror_database and an instance of Customer class
    """
    print("Please input your first Name\n")
    first_name = input_validation('validate_string')

    print("And now your last name\n")
    last_name = input_validation('validate_string')

    new_customer = Customer(first_name, last_name)
    print("The bank welcomes you as a new client\n")

    return new_customer






def create_account_console(new_customer, employee):
    """
    description: Creates an instance of the Account class

    parameter: mirror_database

    return: updated mirror_database and an instance of Account class
    """
    print("What type of account would you like to create? Checking or Savings\n")
    account_type  = input_validation('account_type')
    new_account = Account(new_customer, employee, account_type)
    print("Congratulations, your account was created successfully\n")

    return new_account





def account_operation_console():
    """
    description: performs an operation (deposit or withdraw) using methods from Customer class

    parameter: mirror_database and instance of Customer class

    return: updated mirror_database
    """
    print("Awesome! What operation would you like to do? Deposit or Withdraw\n")
    operation_type = input_validation('operation_type')

    print("Great choice! And which account would you like to operate? Checking or Savings\n")
    account_type  = input_validation('account_type')

    print("How much would you like to deposit or withdraw\n")
    amount = input_validation('validate_integer')

    print("Hooray, your operation was performed beautifully\n")

    return operation_type, account_type, amount






def service_or_loan_console(new_customer):
    """
    description: Creates an instance of the Service class and, if requested, utilizes the request_loan method from Services class

    parameter: mirror_database and instance of Customer class

    return: updated mirror_database
    """
    print("We offer credit-card or loan as services. Which one would you like?\n")
    service_type = input_validation('service_type')
    new_service = Service(service_type, new_customer)

    print("Awesome, all set up\n")
    
    return new_service




def input_validation(validation_type):
    """
    description: This function will validate the user input depending on its type:
                 It can be a string, integer or a simple yes or no

    parameter: Input from the user

    return: the input validate or error message
    """
    if validation_type == 'validate_integer':
        while True:
            try:
                user_input = int(input())
                break
            except ValueError:
                print('Please enter a valid amount\n')


    if validation_type == 'validate_string':
        while True:
            user_input = input()
            if user_input.isalpha():
                break
            else:
                print("Please enter characters A-Z only")



    if validation_type == 'operation_type':
        while True:
            user_input = input().lower()
            if user_input in ['deposit', 'withdraw']:
                break
            else:
                print('Sorry, we only offer DEPOSIT or WITHDRAW. Please choose of one of these.\n')


    if validation_type == 'account_type':
        while True:
            user_input = input().lower()
            if user_input in ['checking', 'savings']:
                break
            else:
                print('Sorry, we only offer CHECKING or SAVINGS. Please choose of one of these.\n')


    if validation_type == 'service_type':
        while True:
            user_input = input().lower().replace('-', '').replace(' ', '')
            if user_input in ['creditcard', 'loan']:
                break
            else:
                print('Sorry, we only offer CREDITCARD or LOAN. Please choose of one of these.\n')


    if validation_type == 'y_n':
        while True:
            user_input = input("y / n: ").lower().replace('yes', 'y').replace('no', 'n')
            if user_input in ['y', 'n']:
                break
            else:
                print('Please select Y or N.\n')


    if validation_type == 'menu':
        while True:
            user_input = input("What would you like to do: ").lower()
            if user_input in ['a', 'b', 'c', 'd']:
                break
            else:
                print('Please select one of the letter in the menu: A, B, C or D\n')



    return user_input
