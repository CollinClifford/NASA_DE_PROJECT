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
    # else:
        # print("we haven't built out anything else yet, dude.")