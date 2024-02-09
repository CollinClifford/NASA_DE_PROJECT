# TODO: Build Services that Trigger Data Factory and ETL process
# TODO: Build Services that Trigger Stored Proceduers

import logging
import subprocess
import os

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Trigger APIs

current_directory = os.path.dirname(os.path.abspath(__file__))
api_trigger = os.path.join(current_directory, 'extraction_scripts/api_extraction.py')
db_trigger = os.path.join(current_directory, 'data_factory/data_factory.py')

try:
    subprocess.run(['python', api_trigger])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')

try:
    subprocess.run(['python', db_trigger])
except Exception as e:
    logging.error(f"One or more subprocesses failed: {e}")