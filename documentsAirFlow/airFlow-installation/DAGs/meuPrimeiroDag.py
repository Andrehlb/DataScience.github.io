from airflow.models import DAG
from airflow.utils.dates import days_ago

# context manager

with DAG(
    'meu_primeiro_dag',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False,
) as dag: