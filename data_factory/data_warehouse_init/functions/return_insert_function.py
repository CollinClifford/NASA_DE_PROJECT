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
    elif web_service == "DONKI/CME":
        try:
            insert_cme_data(cursor, data)
            logging.info('insert_cme_data function triggered successfully.')
        except Exception as e:
            logging.error(f"insert_cme_data function failed: {e}")
    elif web_service == 'DONKI/CMEAnalysis':
        try:
            insert_cme_analysis_data(cursor, data)
            logging.info('insert_cme_analysis_data function triggered successfully')
        except Exception as e:
            logging.error(f"insert_cme_analysis_data function failed: {e}")
    elif web_service == "DONKI/GST":
        try:
            insert_gst_data(cursor, data)
            logging.info('insert_gst_data function triggered successfully.')
        except Exception as e:
            logging.error(f'insert_gst_data function failed: {e}')
    elif web_service == 'DONKI/HSS':
        try:
            insert_hss_data(cursor, data)
            logging.info("insert_hss_data function triggered successfully")
        except Exception as e:
            logging.error(f"insert_hss_data function failed: {e}")
    elif web_service == 'DONKI/IPS':
        try:
            insert_ips_data(cursor, data)
            logging.info('insert_ips_data function triggered successfully')
        except Exception as e:
            logging.error(f'insert_ips_data function failed: {e}')
    elif web_service == 'DONKI/MPC':
        try:
            insert_mpc_data(cursor, data)
            logging.info('insert_mpc_data function triggered successfuly')
        except Exception as e:
            logging.error(f'insert_mpc_data function failed: {e}')
    else:
        return