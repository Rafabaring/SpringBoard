import json
from bank_assignment import *
from bank_assignment_console import *
from dbutils import *

def main():

    # Initiate a database
    mirror_database = OutstandingDatabase()

    # Initiating an instance of Employee customer
    emp_1 = Employee("Kiko", "Loureiro", "Megadeth", "Guitar Player")
    mirror_database.update_partial_database('employee', emp_1.payload)

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

        client_menu_input = input_validation('menu')

        if client_menu_input == "a":
            # Create a new customer
            new_customer = register_customer_console()

            # Update the database with the recently created customer
            mirror_database.update_partial_database('customer', new_customer.payload)





        if client_menu_input == "b":
            # Create a new account
            new_account = create_account_console(new_customer, emp_1)

            # Update the database with the recently created account
            mirror_database.update_partial_database('account', new_account.payload)





        if client_menu_input == "c":
            # Getting the customer input
            operation_type, account_type, amount = account_operation_console()

            # Get the client that will perform the operation
            payload_to_operate = mirror_database.get_client_to_operate(new_customer.id, account_type)

            # Perform the operation in the payload. Returns a new, modified, payload
            payload_operated =  new_customer.account_operation(operation_type, amount, payload_to_operate)

            # Update the database
            mirror_database.update_partial_database('account', payload_operated)





        if client_menu_input == "d":
            # Create a new service
            new_service = service_or_loan_console(new_customer)

            # Update the database
            mirror_database.update_partial_database("service", new_service.payload)

            if new_service.service_type == "loan":
                print("Given you created a loan, would you like to request it?\n")
                loan_y_n = input_validation('y_n')
                if loan_y_n == "y":
                    print("Awesome!, how much would you like to request?\n")
                    # Validating the user input
                    loan_amount = input_validation('validate_integer')
                    payload_to_operate = mirror_database.get_client_to_operate(new_customer.id, "checking")
                    payload_operated = new_service.request_loan(new_customer, loan_amount, payload_to_operate)

                    # Update the database with the recently updated payload
                    mirror_database.update_partial_database('account', payload_operated)
                    print("Congrats! Your loan was approved and the amount requested was deposited in your checking account\n")
                else:
                    print("Cool! No worries :)")

        client_satisfied = is_client_satisfied()

    # When the client is satisfied, they exit the while loop
    print("""
        Thank you for stopping by. Always great to see you here
        """)
    print("This is how the database looks like\n")
    print(mirror_database.data)


    # When all operations are completed and the client is satisfied, the records are added to the database
    # update_database(mirror_database)
    mirror_database.update_database()





if __name__ == "__main__":
    main()
