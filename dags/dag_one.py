from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator



with DAG (
    dag_id = "dag_one",
    start_date = datetime(2025, 10, 3),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
   task_hello = BashOperator(
        task_id = "hello",
        bash_command = 'echo "My name is Ali Moahmed and I am a data engineer and my age is 21. Wellcome to Airflow"'
    ) 