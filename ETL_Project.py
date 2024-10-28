# Import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago
import requests

default_args = {$
    'owner': 'Maryam',
    'start_date': days_ago(0),
    'email': ['immaryamm@yahoo.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)as dag:


    # Task 1:unzip data
    unzip_data = BashOperator(
        task_id='unzip_data',
        bash_command='tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment'
        )

    # Task2: extract specific columns from vehicle-data.csv using cut
    extract_data_from_csv = BashOperator(
        task_id='extract_data_from_csv',
        bash_command="cut -d',' -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv"
        )

    # Task3: extract specific columns from tollplaza-data.tsv using cut
    extract_data_from_tsv = BashOperator(
        task_id='extract_data_from_tsv',
        bash_command="cut -f5-7 < /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv"
        )

    # Task4: extract specific fields from payment-data.txt using cut for fixed width
    extract_data_from_fixed_width = BashOperator(
        task_id='extract_data_from_fixed_width',
        bash_command="cut -c59-62,63-67 /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv"
        ) 

    # Task5: consolidate data from the extracted files
    consolidate_data = BashOperator(
        task_id='consolidate_data',
        bash_command=(
            "paste -d',' /home/project/airflow/dags/finalassignment/csv_data.csv "
            "/home/project/airflow/dags/finalassignment/tsv_data.csv "
            "/home/project/airflow/dags/finalassignment/fixed_width_data.csv "
            "| cut -d',' -f1,2,3,4,5,6,7,8,9 > /home/project/airflow/dags/finalassignment/extracted_data.csv"
            )
        ) 

    # Task6: transform vehicle_type to uppercase and save to transformed_data.csv
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command=(
            "cut -d',' -f4 /home/project/airflow/dags/finalassignment/extracted_data.csv | tr '[:lower:]' '[:upper:]' > /home/project/airflow/dags/finalassignment/transformed_data.csv"
            )
        )


    # Define task dependencies
    unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
    