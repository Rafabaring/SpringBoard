#!/usr/bin/python
import sys


#loading data using stdin - reading from reducer1
for row in sys.stdin:

    # splitting the row into a list
    row_data = row.split('\t')

    # building up the key used in key/value pair
    value = (row_data[1])
    make = value[1]
    year = value[2]
    composite_key = make + year
    print '%s\t%s' % (composite_key, 1)
