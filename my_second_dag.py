from __future__ import annotations

from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator

def decide_next_task(**kwargs):
    # Implement your condition here
    # For example, you can check the current date and decide based on that
    current_date = datetime.now().minute
    if current_date % 2 == 0:
        return "print_date"
    else:
        return "print_date2"
with DAG(
    "my_second_dag",
    default_args={
        "email": ["matheepat.seiya@gmail.com"],
    },
    description="A simple tutorial DAG with a conditional task",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    tags=["example"],
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )
    t2 = BashOperator(
        task_id="print_date2",
        bash_command="date",
    )

    decide_task = BranchPythonOperator(
        task_id="decide_task",
        python_callable=decide_next_task,
    )

    decide_task >> t1
    decide_task >> t2