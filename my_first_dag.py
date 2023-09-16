from __future__ import annotations

# [START tutorial]
# [START import_module]
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
with DAG(
    "my_first_dag",
    default_args={
        "email": ["matheepat.seiya@gmail.com"],
    },
    description="A simple tutorial DAG",
    schedule=None,
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
	t1 >> t2 