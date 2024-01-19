import os
from dotenv import load_dotenv
from functions.return_json import return_json
from functions.append_to_json import append_to_json
from api_keys import web_services
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

today = datetime.now()
last_week = datetime.now() - timedelta(7)
start_date = last_week.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

if __name__ == "__main__":
    try:
        api_key = os.getenv('API_KEY')
    except Exception as e:
        logging.error(f"API Key not found: {e}")

    try: 
        for web_service, unique_id in web_services.items():
            logging.info(web_service)
            # Calls return_json function which makes GET HTTP request and returns JSON for each web service

            try:
                data_json = return_json(web_service, api_key, start_date, end_date)
            except Exception as e:
                logging.error(f"return_json function failed: {e}")

            # Calls append_to_json function which takes the JSON and saves it to local data lake.

            try:
                if web_service == 'neo/rest/v1/feed':
                    append_to_json(data_json, web_service, unique_id)
                else:
                    for entry in data_json:
                        append_to_json(entry, web_service, unique_id)
            except Exception as e:
                logging.error(f"append_to_json function failed: {e}")
            
    except Exception as e:
        logging.error(f"Extraction process failed: {e}")