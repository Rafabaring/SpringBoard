#!/bin/bash
spark-submit \
--master local \
--py-files /Users/rafaelbaring/Documents/SpringBoard/Guided_capstone/load_data.py
&&
spark-submit \
--master local \
--py-files /Users/rafaelbaring/Documents/SpringBoard/Guided_capstone/EOD_job.py
&&
spark-submit \
 --master local \
 --py-files Users/rafaelbaring/Documents/SpringBoard/Guided_capstone/analytical_job.py
