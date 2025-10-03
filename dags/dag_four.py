from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="dag_four",
    default_args=default_args,
    start_date=datetime(2025, 10, 3),
    schedule_interval=timedelta(minutes=2),
    catchup=False,
    tags=["postgres"]
) as dag:

    create_table = PostgresOperator(
        task_id="create_table_task",
        postgres_conn_id="postgres_conn",
        sql="""
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    insert_row = PostgresOperator(
        task_id="insert_row_task",
        postgres_conn_id="postgres_conn",
        sql="INSERT INTO my_table (name) VALUES ('Hello from Airflow');"
    )

    select_rows = PostgresOperator(
        task_id="select_rows_task",
        postgres_conn_id="postgres_conn",
        sql="SELECT * FROM my_table;"
    )

    create_table >> insert_row >> select_rows
