import psycopg2
import json
from dotenv import load_dotenv
import os
import logging
from sql_commands.create_table import *
from sql_commands.drop_table import *
from functions.return_path import return_path
from functions.web_services import web_services
from functions.return_insert_function import return_insert_function

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

current_script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))


# Connects to DB, runs drop, create, and insert functions and closes connection.
def main():

    try:
        load_dotenv()
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        ssl_mode = os.getenv("SSL_MODE")

        db_params = {
            'host': db_host,
            'database': db_name,
            'user': db_user,
            'password': db_password,
            'port': db_port,
            'sslmode': ssl_mode
        }

        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        logging.info("Connection successful.")

        # Runs through array of drop table functions and triggers them.
        try:
            dt_apod(cursor)
            dt_cme(cursor)
            dt_cme_analysis(cursor)
            dt_gst(cursor)
            dt_hss(cursor)
            dt_ips(cursor)
            dt_mpc(cursor)
            dt_notifications(cursor)
            dt_rbe(cursor)
            dt_sep(cursor)
            dt_wsaenlilsimulations(cursor)
            dt_earth(cursor)
            dt_epic_enhanced(cursor)
            dt_epic_natural(cursor)
            dt_mars_rover_photos_curiosity(cursor)
            dt_mars_rover_photos_opportunity(cursor)
            dt_mars_rover_photos_perseverance(cursor) 
            dt_mars_rover_photos_spirit(cursor)
            dt_neows(cursor)
            logging.info(f"Tables Successfully Dropped.")
        except Exception as e:
            logging.error(f"An error occured while dropping table: {e}")

        # Runs through array of create table functions and triggers them.
        try:
            ct_apod(cursor)
            ct_cme(cursor)
            ct_cme_analysis(cursor)
            ct_gst(cursor)
            ct_hss(cursor)
            ct_ips(cursor)
            ct_mpc(cursor)
            ct_notifications(cursor)
            ct_rbe(cursor)
            ct_sep(cursor)
            ct_wsaenlilsimulations(cursor)
            ct_earth(cursor)
            ct_epic_enhanced(cursor)
            ct_epic_natural(cursor)
            ct_mars_rover_photos_curiosity(cursor)
            ct_mars_rover_photos_opportunity(cursor)
            ct_mars_rover_photos_perseverance(cursor)
            ct_mars_rover_photos_spirit(cursor)
            ct_neows(cursor)
            logging.info("Tables Successfully created.")
        except Exception as e:
            logging.error(f"An error occured while creating table: {e}")

        for web_service in web_services:
            json_file_path = return_path(web_service, project_directory)

            with open(json_file_path, 'r') as file:
                json_data = json.load(file)
                
            for record in json_data:
                return_insert_function(web_service, cursor, record)
                
        conn.commit()
        conn.close()

    except Exception as e:
        logging.error(f"An error occurred while connecting to database: {e}")

if __name__ == "__main__":
    main()