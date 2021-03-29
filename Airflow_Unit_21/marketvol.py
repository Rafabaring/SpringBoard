from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import date, datetime, timedelta

import yfinance as yf
import pandas as pd

default_args = {
            "owner": "airflow",
            "start_date": datetime(2021, 3, 24),
            "depends_on_past": False,
            "email_on_failure": False,
            "retries": 2, # retry twice
            "retry_delay": timedelta(minutes=5) # five minutes interval
        }


def download_stock_data(stock_name):
    start_date = date.today()
    end_date = start_date + timedelta(days=1)
    df = yf.download(stock_name, start=start_date, end=end_date, interval='1m')
    df.to_csv(stock_name + "_data.csv" header=False)


def get_last_stock_spread():
    apple_data = pd.read_csv("tmp/data/AAPL_data.csv").sort_values(by = "date time", ascending = False)
    tesla_data = pd.read_csv("tmp/data/TSLA_data.csv").sort_values(by = "date time", ascending = False)
    spread = [apple_data['high'][0] - apple_data['low'][0], tesla_data['high'][0] - tesla_data['low'][0]]
    return spread


with DAG(dag_id="marketvol",
         schedule_interval="6 0 * * 1-5", # running at 6pm for weekdays
         default_args=default_args,
         description='source Apple and Tesla data' ) as dag:

    task_0 = BashOperator(
        task_id="task_0",
        bash_command='''mkdir -p /tmp/data/''' + date.today() #naming the folder with the current day
    )

    # download and save TESLA data
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=download_stock_data('TSLA')
    )

    # download and save APPLE data
    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=download_stock_data('AAPL')
    )


    # moving data to hadoop environment - focusing on TESLA data
    task_3 = BashOperator(
        task_id="task_3",
        bash_command='''mv TSLA_data.csv /tmp/data/''' + date.today() + '''$HADOOP_HOME/bin/hadoop/''' + date.today()
    )

    # moving data to hadoop environment - focusing on APPLE data
    task_4 = BashOperator(
        task_id="task_4",
        bash_command='''mv TSLA_data.csv /tmp/data/''' + date.today() + '''$HADOOP_HOME/bin/hadoop/''' + date.today()
    )

    task_5 = PythonOperator(
        task_id="task_5",
        python_callable=get_last_stock_spread('AAPL')
    )

# Setting job dependencies
task_0 >> [task_1, task_2] >> [task_3, task_4] >> task_5
