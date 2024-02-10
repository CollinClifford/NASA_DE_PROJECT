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
    if data['linkedEvents'] == None:
        linkedEvents = None
    else:
        linkedEvents = json.dumps(data['linkedEvents'])

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

    columns = data.keys()
    values = [data[column] for column in columns]

    insert_query = f"""
        INSERT INTO donki.cme_analysis_raw ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    cursor.execute(insert_query, values)

def insert_gst_data(cursor, data):
    gstId = data['gstID']
    startTime = data['startTime']
    if data['allKpIndex'] == None:
        allKpIndex = None
    else:
        allKpIndex = json.dumps(data['allKpIndex'])
    if data['linkedEvents'] == None:
        linkedEvents = None
    else:
        linkedEvents = json.dumps(data['linkedEvents'])
    link = data['link']

    insert_query = """
        INSERT INTO donki.gst_raw (
        gstId,
        startTime,
        allKpIndex,
        linkedEvents,
        link
        ) VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (gstId, startTime, allKpIndex, linkedEvents, link))

def insert_hss_data(cursor, data):
    hssID = data['hssID']
    eventTime = data['eventTime']
    if data['instruments'] == None:
        instruments = None
    else:
        instruments = json.dumps(data['instruments'])
    if data['linkedEvents'] == None:
        linkedEvents = None
    else:
        linkedEvents = json.dumps(data['linkedEvents'])
    link = data['link']

    insert_query = """
        INSERT INTO donki.hss_raw (
        hssID,
        eventTime,
        instruments,
        linkedEvents,
        link
        ) VALUES (%s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (hssID, eventTime, instruments, linkedEvents, link))

def insert_ips_data(cursor, data):
    catalog = data['catalog']
    activityID = data['activityID']
    location = data['location']
    eventTime = data['eventTime']
    link = data['link']
    if data['instruments'] == None:
        instruments = None
    else:
        instruments = json.dumps(data['instruments'])

    insert_query = """
        INSERT INTO donki.ips_raw (
        catalog,
        activityID,
        location,
        eventTime,
        link,
        instruments
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (catalog, activityID, location, eventTime, link, instruments))