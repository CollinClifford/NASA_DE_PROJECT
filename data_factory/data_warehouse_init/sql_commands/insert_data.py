import json

def insert_apod_data(cursor, data):
    columns = data.keys()
    values = [data[column] for column in columns]

    insert_query = f"""
        INSERT INTO apod.apod_raw ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    cursor.execute(insert_query, values)

def insert_neows_data(cursor, data):

    date = data['date']
    data_json = json.dumps(data)

    insert_query = f"""
        INSERT INTO neows.neows_raw (date, objects)
        VALUES (%s, %s);
        """

    cursor.execute(insert_query, (date, data_json))