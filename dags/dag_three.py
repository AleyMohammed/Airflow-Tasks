from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator

from airflow.operators.python_operator import PythonOperator

def loop_nums():
    for i in range(10):
        print(i)


with DAG (
    dag_id = "dag_three",
    start_date = datetime(2025, 10, 3),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task_loop = PythonOperator(
        task_id = "loop",
        python_callable = loop_nums
    )

task_loop