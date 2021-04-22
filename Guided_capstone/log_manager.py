from datetime import date
import config as cfg


current_date = date.today().strftime("%d-%m-%Y")
# Reading from file
def log_daily_records(rdd_to_log, state):

    log = open("/Users/rafaelbaring/Documents/GitHub/SpringBoard/Guided_capstone/daily_log/" + state + "_daily_log_" + current_date + ".txt", "w+")
    log.write(str(rdd_to_log))
    log.close()
    print("\nfile logged into local directory\n")


import boto3
import boto3.s3
import sys
# from boto3.s3.key import Key
def log_daily_records_s3(file, bucket, object_name=None):

    AWS_ACCESS_KEY_ID = cfg.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = cfg.AWS_SECRET_ACCESS_KEY

    s3_client = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3_client.upload_file(file, bucket, object_name)
    print("\nfile logged into cloud directory\n")


def log_rejected_rows(row_to_log):
    log = open("/Users/rafaelbaring/Documents/GitHub/SpringBoard/Guided_capstone/daily_log/rejected_row/rejected_log_" + current_date + ".txt", "w+")
    log.write(row_to_log)
