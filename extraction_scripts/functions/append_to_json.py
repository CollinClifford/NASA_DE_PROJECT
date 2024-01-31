import os
import json
import logging
from functions.return_path import return_path

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# This function locates the JSON
# file and appends the HTTP Request
# to the selected file

def append_to_json(data, web_service, unique_id):

    existing_data = []

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))

    # Loads the proper JSON based on the API call.
    json_file_path = return_path(web_service, project_directory)

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        logging.error(f"Error loading existing data: {e}")

    # Special case for NeoWs
    if 'near_earth_objects' in data:
        try:
            neo_objects = data['near_earth_objects']
            
            for date, objects_list in neo_objects.items():
                existing_dates = [entry.get('date') for entry in existing_data]
                if date not in existing_dates:
                    existing_data.append({'date': date, 'objects': objects_list})
                    logging.info(f"Data for date {date} appended successfully.")
                else:
                    logging.info(f"Data for date {date} already exists. Skipping append.")
                    
            with open(json_file_path, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=2)
        
        except Exception as e:
            logging.error(f'append_to_json failed to append: {e}')

    # Special case for Mars Photos
    elif 'photos' in data:
        try:
            photos = data['photos']
            
            for id, objects_list in photos.items():
                existing_dates = [entry.get(unique_id) for entry in existing_data]
                if id not in existing_dates:
                    existing_data.append(data)
                    logging.info(f"Data for date {id} appended successfully.")
                else:
                    logging.info(f"Data for date {id} already exists. Skipping append.")
                    
            with open(json_file_path, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=2)
        
        except Exception as e:
            logging.error(f'append_to_json failed to append: {e}')
    
    # Searches for Unique_ID and appends JSON information.            
    else:
        try:
            existing_dates = [entry.get(unique_id) for entry in existing_data]
            if data[unique_id] not in existing_dates:
                existing_data.append(data)
                with open(json_file_path, 'w', encoding='utf-8') as file:
                    json.dump(existing_data, file, indent=2)
                logging.info("Data appended successfully.")
            else:
                logging.info(f"Data with date {data[unique_id]} already exists. Skipping append.")
                
        except Exception as e:
            logging.error(f'append_to_json failed to append: {e}')