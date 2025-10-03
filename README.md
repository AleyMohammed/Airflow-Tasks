# Airflow-Tasks
This repo contains four different tasks using Airflow.

## DAGs Overview
# DAG 1:
A simple DAG that prints my name and a brief self-introduction. This demonstrates a basic Airflow task and Python function execution.
- code :
<img width="2110" height="976" alt="Image" src="https://github.com/user-attachments/assets/17813592-50c6-4565-9b5f-60a4271a881d" />

----------------------------------------------------------------------------------------------------------------------------------------
- files :
<img width="287" height="242" alt="Image" src="https://github.com/user-attachments/assets/8cf1d431-b658-452f-a426-bce2fb34537a" />

----------------------------------------------------------------------------------------------------------------------------------------
- Graph :
<img width="1894" height="735" alt="Image" src="https://github.com/user-attachments/assets/8d9d4f65-d31e-4a6c-bef8-3c0159a18d18" />
----------------------------------------------------------------------------------------------------------------------------------------



- Logs :
<img width="1456" height="217" alt="Image" src="https://github.com/user-attachments/assets/af4ac3fb-4ca6-48b7-a663-d05b83371473" />



<img width="1682" height="89" alt="Image" src="https://github.com/user-attachments/assets/a3938642-1897-4c27-b9cb-c8b345d3240a" />

# DAG 2:
A DAG consisting of two tasks connected together, showing the use of task dependencies and direct workflow relations inside Airflow. Each task is executed in sequence.
- code :
  <img width="2388" height="1166" alt="Image" src="https://github.com/user-attachments/assets/d1f8aad2-92b0-4f37-a542-d9831bdcdd8b" />


----------------------------------------------------------------------------------------------------------------------------------------
- Graph :
<img width="1872" height="586" alt="Image" src="https://github.com/user-attachments/assets/665a732a-8323-4e5d-a678-66e5feb39698" />
  

----------------------------------------------------------------------------------------------------------------------------------------

- Logs :
  <img width="1465" height="293" alt="Image" src="https://github.com/user-attachments/assets/fa98cd43-cc14-41ec-baf3-f1a68575bcb9" />




 
# DAG 3:
This DAG features a Python function that is called as an Airflow task. It showcases how to use the PythonOperator to run custom Python code inside an Airflow DAG.

- Code : 
<img width="1234" height="1166" alt="Image" src="https://github.com/user-attachments/assets/a7385287-4a3e-4bae-b769-4e06c9a5afd0" />

-------------------------------------------------------------------------------------------------------------------------------------

- Graph :
<img width="1474" height="499" alt="Image" src="https://github.com/user-attachments/assets/cd46c9a0-4a82-4ec3-a6a6-7b72d47f0aad" />

-------------------------------------------------------------------------------------------------------------------------------------

- Logs :
<img width="1457" height="406" alt="Image" src="https://github.com/user-attachments/assets/17488199-6807-44e4-902a-ac214c9c7471" />




# DAG 4:
The last DAG is based on Postgres. It uses PostgresOperators to perform database operations such as creating a table, inserting a row, and selecting data. This example highlights database integration with Airflow.


- Code : 
<img width="1448" height="2002" alt="Image" src="https://github.com/user-attachments/assets/f21f55d1-b12a-4631-9b86-27daac42b699" />

-------------------------------------------------------------------------------------------------------------------------------------


- Files :
<img width="295" height="301" alt="Image" src="https://github.com/user-attachments/assets/7bbe29da-8f3c-4075-8ce4-92d79d7717a1" />

-------------------------------------------------------------------------------------------------------------------------------------

- Graph :
<img width="1466" height="644" alt="Image" src="https://github.com/user-attachments/assets/4ea94db7-4bfb-4a7d-8eb2-0c461fe26787" />
-------------------------------------------------------------------------------------------------------------------------------------


- Logs :
<img width="930" height="467" alt="Image" src="https://github.com/user-attachments/assets/9330329b-953e-4a38-a9a6-1cceecca984e" />

-------------------------------------------------------------------------------------------------------------------------------------

- All Dags : 
<img width="1877" height="357" alt="Image" src="https://github.com/user-attachments/assets/27a57ab5-3529-4442-9952-0905115ec3b4" />
