#!/usr/bin/python
import sys

result_key = None
result_list = []

def reset():
    # Defining global variables - group level master info
    global result_key, result_list

    # "Empty" global variable
    result_key = None
    result_list = []


#Run for end of every group
def flush():
    global result_key, result_list
    total = 0

    # loop throught each one of the records
    for value in result_list:
        # adding up number of occurrences
        total += value

# interating throght the data resulted from the mapper
# key is composed key with make and year
for row in sys.stdin:
    # [parse the input we got from mapper and update the master info]
    row_data = row.split('\t')
    key = row_data[0]
    value = int(row_data[1])

    # detect key changes
    if result_key != key:
        if result_key != None:
            flush()
        reset()
    # update more master info after the key change handling
    result_list.append(value)
    result_key = key

# do not forget to output the last group if needed!
flush()
