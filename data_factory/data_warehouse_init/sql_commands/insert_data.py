import json
from psycopg2.extras import Json
from psycopg2.extensions import register_adapter

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

def insert_cme_data(cursor, data):

    activityID = data['activityID']
    catalog = data['catalog']
    startTime = data['startTime']
    sourceLocation = data['sourceLocation']
    activeRegionNum = data['activeRegionNum']
    link = data['link']
    note = data['note']
    if data['instruments'] == None:
        instruments = None
    else:
        instruments = json.dumps(data['instruments'])
    if data['cmeAnalyses'] == None:
        cmeAnalyses = None
    else:
        cmeAnalyses = json.dumps(data['cmeAnalyses'])
    linkedEvents = data['linkedEvents']

    insert_query = """
        INSERT INTO donki.cme_raw (
        activityID,
        catalog, 
        startTime,
        sourceLocation, 
        activeRegionNum,
        link, 
        note, 
        instruments, 
        cmeAnalyses, 
        linkedEvents
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, (activityID, catalog, startTime, sourceLocation, activeRegionNum, link, note, instruments, cmeAnalyses, linkedEvents))

def insert_cme_analysis_data(cursor, data):
    # print(data)
    # insert_query = """
    #     INSERT INTO donki.cme_analysis_raw (
    #     time21_5,
    #     latitude, 
    #     longitude,
    #     halfAngle, 
    #     speed,
    #     type, 
    #     isMostAccurate, 
    #     associatedCMEID, 
    #     note, 
    #     catalog,
    #     link
    #     )
    #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    # """
    # cursor.execute(insert_query, data)
    columns = data.keys()
    values = [data[column] for column in columns]

    insert_query = f"""
        INSERT INTO donki.cme_analysis_raw ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    cursor.execute(insert_query, values)