import logging
import subprocess
import os

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Trigger Database Initialization.

current_directory = os.path.dirname(os.path.abspath(__file__))
db_init_trigger = os.path.join(current_directory, 'data_warehouse_init/database_init.py')

try:
    subprocess.run(['python', db_init_trigger])
except Exception as e:
    logging.error(f'One or more subprocesses failed at the data factory level: {e}')
