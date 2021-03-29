from pyspark import SparkConf, SparkContext

# Starting the spark context
conf = SparkConf().setMaster("local").setAppName("optimize_post_sale")
sc = SparkContext(conf = conf)

path_to_data = '/Users/rafaelbaring/Documents/SpringBoard/Spark_Unit_20/data.csv'
lines = sc.textFile(path_to_data)

# Parse the lines coming from the raw data
def extract_vin_key_value(line):
    '''
    Parse each line coming from the raw data
    '''
    fields = line.split(',')

    accident_type = str(fields[1])
    vin_number = str(fields[2])
    make = str(fields[3])
    year = str(fields[5])
    return (vin_number, [accident_type, make, year])


def analyze_make_model(list):
    '''
    Check if an accidente happened for a specific VIN and assign the make and year values
    for that VIN
    '''
    for i in list[0]:
        # Checking if an accident occured
        if i == 'A':
            # Make and year is inside the first list of the value. The count is in the second
            make = list[0][1]
            year = list[0][2]
            count = int(list[1])
            # Build the returning object following the requirements
            return (make + " - " + year, count)


# Starting the spark transformation

# Creating and reducing original RDD
rdd = lines.map(extract_vin_key_value)
rdd_unique_vin = rdd.mapValues(lambda x: (x,1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Extrapolating make and year to accidente level data
rdd_clean = rdd_unique_vin.mapValues(lambda x: analyze_make_model(x)).values().collect()
# rdd_clean = rdd_clean

# Creating a new RDD only with records that have an accidents. Records without accident will be explicit as None
clean_list = [clean_value for clean_value in rdd_clean if clean_value != None]
rdd_data = sc.parallelize(clean_list).reduceByKey(lambda a, b: a + b)
results = rdd_data.collect()
for result in results:
    print(result)
