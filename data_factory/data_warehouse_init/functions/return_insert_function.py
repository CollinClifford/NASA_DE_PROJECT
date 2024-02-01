from sql_commands.insert_data import *
import logging

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def return_insert_function(web_service, cursor, data):
    if web_service == "planetary/apod":
        try:
            insert_apod_data(cursor, data)
            logging.info("insert_apod_data function triggered successfully.")
        except Exception as e:
            logging.error(f"insert_apod_data function failed: {e}")
    elif web_service == "neo/rest/v1/feed":
        try:
            insert_neows_data(cursor, data)
            logging.info("insert_neows_data function triggered successfully.")
        except Exception as e:
            logging.error(f"insert_neows_data function failed: {e}")
    else:
        return