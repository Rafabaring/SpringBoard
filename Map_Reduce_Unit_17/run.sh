#/bin/bash
echo "Running FIRST set of mapper and reducer"

PATH_TO_JAR=/path/to/hadoop_jar_file/hadoop-streaming-3.2.1.jar

hadoop jar $PATH_TO_JAR \
-file autoinc_mapper1.py -mapper autoinc_mapper1.py \
-file autoinc_reducer1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents

echo "------!-----"
echo "Running SECOND set of mapper and reducer"

hadoop jar $PATH_TO_JAR \
-file autoinc_mapper2.py -mapper autoinc_mapper2.py \
-file autoinc_reducer2.py -reducer autoinc_reducer2.py \
-input output/all_accidents -output output/make_year_count
