def insert_apod_data(cursor, data):
    columns = data.keys()
    values = [data[column] for column in columns]

    insert_query = f"""
        INSERT INTO apod.apod_raw ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    cursor.execute(insert_query, values)

