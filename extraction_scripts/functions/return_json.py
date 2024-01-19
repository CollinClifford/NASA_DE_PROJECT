import requests
import logging
from functions.return_params import return_params

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def return_json(web_service, api_key, start_date, end_date):

    json = {}
    if web_service == 'EPIC/api/natural/date/':
        url = f'https://api.nasa.gov/EPIC/api/natural/date/{start_date}'
    elif web_service == 'EPIC/api/enhanced/date/':
        url = f'https://api.nasa.gov/EPIC/api/enhanced/date/{start_date}'
    else:
        url = f"https://api.nasa.gov/{web_service}"

    # Condition to properly load API parameters.

    params = return_params(web_service, start_date, end_date, api_key)

    try:

        # Returns JSON for loaded web_service.

        response = requests.get(url, params=params)

        if response.status_code == 200:
            json = response.json()
            return json
        else:
            logging.error(f"HTTP response: {response.status_code}")

    except Exception as e:
        logging.error(f"Request error: {e}")