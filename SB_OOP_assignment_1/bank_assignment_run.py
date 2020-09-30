import json
from bank_assignment import *
from bank_assignment_console import *
from bank_custom_lib import update_database, initiate_database, get_id, update_partial_database

def main():

    # Initiate a database
    initiate_database()

    # Open the database to run operations on it
    with open('database.txt', 'r+') as database:
        mirror_database = json.load(database)
        database.close()

    # Initiating an instance of Employee customer
    emp_1 = Employee("Kiko", "Loureiro", "Megadeth", "Guitar Player")
    mirror_database = update_partial_database('employee', emp_1.payload, mirror_database)
    print('')
    print('')

    client_satisfied  = 'n'
    while client_satisfied ==  'n':
        print("""
        Hello, I'm the manager of this branch
        These are our services today. How can I help you?

        A) Register as a customer
        B) Create an account
        C) Deposit or Withdraw
        D) Request a Service or a Loan

        please reply with one of the letter (A, B, C, D)
        """)

        # system is case NOT sensitive
        client_menu_input = input().lower()

        if client_menu_input == "a":
            new_customer, mirror_database = register_customer_console(mirror_database)

        if client_menu_input == "b":
            mirror_database = create_account_console(new_customer, emp_1, mirror_database)

        if client_menu_input == "c":
            mirror_database = account_operation_console(new_customer, mirror_database)

        if client_menu_input == "d":
            mirror_database = service_or_loan_console(new_customer, mirror_database)

        # print(mirror_database)
        client_satisfied = is_client_satisfied()

    # When the client is satisfied, they exit the while loop
    print("""
        Thank you for stopping by. Always great to see you here
        """)
    print("This is how the database looks like\n")
    print(mirror_database)


    # When all operations are completed and the client is satisfied, the records are added to the database
    update_database(mirror_database)





if __name__ == "__main__":
    main()
