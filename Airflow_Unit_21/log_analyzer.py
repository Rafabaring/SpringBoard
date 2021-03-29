

# base_log_folder = "/Users/rafaelbaring/airflow/logs" MUDAR PRA ESSE ANTES DE SUBIR O CODIGO
base_log_folder = "/Users/rafaelbaring/Documents/SpringBoard/Airflow_Unit_21/log.txt"

def analyze_file(path_to_log):
    '''
    This function was designed to analyze ERROR log from Airflow
    Input:
        path to the log file: should follow this pattern:
        /Users/your_computer_user_name/airflow/logs

    Output:
        count of all errors in the file
        list of the errors in the file
    '''
    # Reading the file from the path provided
    f = open(base_log_folder, "r")
    log = f.read()

    # Splitting the log file in a list
    # One row per list
    log_list = log.split('\n')

    # Looping through the log list and finding ERRORS
    # For this exercises, I understand that ERRORS can be found with the string " ERROR - "
    error_string = " ERROR - "
    log_error_list = []
    for log in log_list:
        if error_string in log:
            log_error_list.append(log)

    # Checking if there's no error
    if not log_error_list:
        print('Congrats! No ERROR in the log')
        error_count = 0

    error_count = len(log_error_list)

    # if " ERROR - " in log_list[85]:
    #     print("JABBA")
    #
    # print(log_list[85])
    return error_count, log_error_list

count, cur_list = analyze_file(base_log_folder)

print(count)
for error_log in cur_list:
    print(error_log)
