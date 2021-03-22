#!/usr/bin/python
import sys

# We are using the VIN number as key
# value is a list of type, make and year
key_value_pair = {}
result_key = None
result_list = []


def reset():
    # Defining global variables - group level master info
    global key_value_pair, result_key, result_list

    # "Empty" global variable
    key_value_pair = {}
    result_key = None
    result_list = []

# Run for end of every group
def flush():
    global key_value_pair, result_key, result_list

    # loop throught each one of the records
    for value in result_list:
        incident_type = value[0]
        # select only the ones that are accident
        # these should have make, year empty
        if incident_type == 'A':
            # assign a value for empty make and year
            make = key_value_pair[result_key][1]
            year = key_value_pair[result_key][2]
            # create the value from key/value pai
            value = (incident_type, make, year)

# interating throght the data resulted from the mapper
for row in sys.stdin:
    # [parse the input we got from mapper and update the master info]
    row_data = row.split('\t')
    key = row_data[0]
    value = (row_data[1])

    # we want to get the make and year as value if the incident type is I
    # detect key changes
    incident_type = value[0]
    if incident_type == 'I':
        key_value_pair[key] = value
    if result_key != key:
        if result_key != None:
            flush()
        reset()
    # update master info after key change
    result_list.append(value)
    result_key = key

# do not forget to output the last group if needed!
flush()
