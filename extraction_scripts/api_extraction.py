import os
from dotenv import load_dotenv
from functions.return_json import return_json
from functions.append_to_json import append_to_json
from api_keys import web_services
from datetime import datetime, timedelta
import logging
from api_keys import lat_long

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
            # Condition to add lattitude and longitude, if the API needs it.
            if web_service == 'planetary/earth/assets':
                # Circle through the lattitude and longitude for the 10 largest cities and plugs them into the params.
                for city, location in lat_long.items():
                    try:
                        data_json = return_json(web_service, api_key, start_date, end_date, location['lat'], location['lon'])
                    except Exception as e:
                        logging.error(f"return_json function failed: {e}")
                    try:
                        append_to_json(data_json, web_service, unique_id)
                    except Exception as e:
                        logging.error(f"append_to_json function failed: {e}")

            # Runs all APIs except Earth API.
            else:
                try:
                    data_json = return_json(web_service, api_key, start_date, end_date, None, None)
                except Exception as e:
                    logging.error(f"return_json function failed: {e}")
                try:
                    # Conditions to iterate through the JSON if it is the neows API.
                    if web_service == 'neo/rest/v1/feed':
                        append_to_json(data_json, web_service, unique_id)
                    else:
                        for entry in data_json:
                            append_to_json(entry, web_service, unique_id)
                except Exception as e:
                    logging.error(f"append_to_json function failed: {e}")
            
    except Exception as e:
        logging.error(f"Extraction process failed: {e}")