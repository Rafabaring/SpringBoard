# Banking system simulation:
## This is OOP exercise for SpringBoard Data Engineering bootcamp

The idea behind this project is to exercise some of the OOP  techniques learned throughtout this course.


### Here you will find:
* **bank_assignment_run.py:**
This is the main file, the one you should run. It controls all interaction the user have with the system

* **bank_assignment_console.py:**
It contains all functions, used by 'bank_assignment_run.py', to call the system's class

* **bank_assignment.py:**
This is the main file. Here it contains all classess from this exercise and the imports needed to run the program

* **dbutils.py:**
All the supporting functions that run outside classes can be found here. Special note is that the function simulating the database initialization lives here as dbutils

* **database.py:**
A simple txt file that simulates the database. When the program completes running, you should find a JSON format string with all informations from all tables. Here is an example:

```{"customer": [
      {"id": 0, "first_name": "name1", "last_name": "l_name1"},
      {"id": 1, "first_name": "name2", "last_name": "l_name2"},
      {"id": 2, "first_name": "name3", "last_name": "l_name3"}
      ],
    "account": [
      {"id": 0, "customer_id": 0, "manager_id": 0, "account_type": "savings", "balance": 1348}, {"id": 1, "customer_id": 1, "manager_id": 0, "account_type": "savings", "balance": 342}
      ],
    "employee": [
      {"id": 0, "first_name": "emp_name1", "last_name": ";l_emp_name1", "branch": "SF", "role": "Manager"},
      {"id": 1, "first_name": "emp_name2", "last_name": "l_emp_name12", "branch": "SF", "role": "Manager"}
      ],
    "service": [
      {"id": 0, "customer_id": 2, "service_type": "loan"}
      ]}
```
### How to run the program:
You can run using command line. Make sure you are in the current path and run the following command:
> python bank_assignment.py

## Important:
Make sure you have a .txt file called "database.txt" in the same directory. Otherwise it will raise an I/O error (this is handled in initiate_database() function in the custom library)
