import psycopg2
import json
from dotenv import load_dotenv
import os
import logging
from sql_commands.create_table import *

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

        create_table_array = [
            ct_apod(cursor)
            , ct_neows(cursor)
            , ct_cme(cursor)
            , ct_cme_analysis(cursor)
            , ct_gst(cursor)
            , ct_hss(cursor)
            , ct_ips(cursor)
            , ct_mpc(cursor)
            , ct_notifications(cursor)
            , ct_rbe(cursor)
            , ct_sep(cursor)
            , ct_wsaenlilsimulations(cursor)
            , ct_earth(cursor)
            , ct_epic_enhanced(cursor)
            , ct_epic_natural(cursor)
            , ct_mars_rover_photos_curiosity(cursor)
            , ct_mars_rover_photos_opportunity(cursor)
            , ct_mars_rover_photos_perseverance(cursor)
            , ct_mars_rover_photos_spirit(cursor)
            , ct_neows(cursor)
        ]

        # runs through array of create table functions and triggers them.
        for ct in create_table_array:
            try:
                ct
            except Exception as e:
                logging.error(f"An error occured while creating table: {e}")

        conn.commit()
        conn.close()

    except Exception as e:
        logging.error(f"An error occurred while connecting to database: {e}")

if __name__ == "__main__":
    main()