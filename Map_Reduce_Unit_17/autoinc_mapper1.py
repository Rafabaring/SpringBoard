#!/usr/bin/python
import sys


#loading data using stdin
for row in sys.stdin:

    # splitting the row into a list
    row_data = row.split(',')

    # vin number used for key
    vin_number = row_data[2]

    # building up the value used in key/value pair
    incident_type = row_data[1]
    make = row_data[3]
    year = row_data[5]
    value = (incident_type, make, year)
    print '%s\t%s' % (vin_number, value)
