'''
Optimize the query plan

Suppose we want to compose query in which we get for each question also the number of answers to this question for each month. See the query below which does that in a suboptimal way and try to rewrite it to achieve a more optimal plan.
'''


import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, month

import os


spark = SparkSession.builder.appName('Optimize I').getOrCreate()


base_path = os.getcwd()

project_path = ('/').join(base_path.split('/')[0:-3])

# answers_input_path = os.path.join(project_path, 'data/answers')
# questions_input_path = os.path.join(project_path, 'output/questions-transformed')

answers_input_path = '/Users/rafaelbaring/Documents/SpringBoard/Spark_Unit_20/data/answers'
questions_input_path = '/Users/rafaelbaring/Documents/SpringBoard/Spark_Unit_20/data/questions'

answersDF = spark.read.option('path', answers_input_path).load()
questionsDF = spark.read.option('path', questions_input_path).load()

# sc = spark.SparkContext


'''
Answers aggregation

Here we : get number of answers per question per month
'''
answers_month = answersDF.withColumn('month', month('creation_date')).groupBy('question_id', 'month').agg(count('*').alias('cnt'))

resultDF = questionsDF.join(answers_month, 'question_id').select('question_id', 'creation_date', 'title', 'month', 'cnt')

resultDF.orderBy('question_id', 'month').show()

'''
Task:

see the query plan of the previous result and rewrite the query to optimize it
'''
# Steps to optimize the query:
# Rewritting to use RDD
# Rewritting to apply *ByKey operators - this will impact the number of shuffles in the query
# Fine tunning the number of partitions
# Executing the requested data with less data structured involved
sc = SparkContext.getOrCreate()

# Selecting the data needed for this exercise
filter_values = answersDF.withColumn('month', month('creation_date')).select('month', 'question_id')

# Creating the RDD
filter_values_rdd = filter_values.rdd.map(tuple)

# Reducing to the value requested in the exercise. Also selecting the number of partitions
filter_values_results = filter_values_rdd.map(lambda x: (x,1)).reduceByKey(lambda a, b: a+b, numPartitions = 4)

# Calling the action once to minimize computational effort
print(filter_values_results.take(10))
