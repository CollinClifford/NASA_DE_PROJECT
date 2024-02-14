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
    return
    # date = data['date']
    # data_json = json.dumps(data)

    # insert_query = f"""
    #     INSERT INTO neows.neows_raw (date, objects)
    #     VALUES (%s, %s);
    #     """

    # cursor.execute(insert_query, (date, data_json))

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

def insert_mpc_data(cursor, data):
    
    mpcID = data['mpcID']
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
        INSERT INTO donki.mpc_raw (
        mpcID,
        eventTime,
        instruments,
        linkedEvents,
        link
        ) VALUES (%s, %s, %s, %s, %s)
        """

    cursor.execute(insert_query, (mpcID, eventTime, instruments, linkedEvents, link))

def insert_notifications_data(cursor, data):

    columns = data.keys()
    values = [data[column] for column in columns]

    insert_query = f"""
        INSERT INTO donki.notifications_raw ({', '.join(columns)})
        VALUES ({', '.join(['%s' for _ in range(len(columns))])});
        """
    
    cursor.execute(insert_query, values)

def insert_rbe_data(cursor, data):
    
    rbeID = data['rbeID']
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
        INSERT INTO donki.rbe_raw (
        rbeID,
        eventTime,
        instruments,
        linkedEvents,
        link
        ) VALUES (%s, %s, %s, %s, %s)
        """

    cursor.execute(insert_query, (rbeID, eventTime, instruments, linkedEvents, link))

def insert_sep_data(cursor, data):
    
    sepID = data['sepID']
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
        INSERT INTO donki.sep_raw (
        sepID,
        eventTime,
        instruments,
        linkedEvents,
        link
        ) VALUES (%s, %s, %s, %s, %s)
        """

    cursor.execute(insert_query, (sepID, eventTime, instruments, linkedEvents, link))

def insert_wsaenlilsimulations_data(cursor, data):
    
    simulationID = data['simulationID']
    modelCompletionTime = data['modelCompletionTime']
    au = data['au']
    if data['cmeInputs'] == None:
        cmeInputs = None
    else:
        cmeInputs = json.dumps(data['cmeInputs'])
    estimatedShockArrivalTime = data['estimatedShockArrivalTime']
    estimatedDuration = data['estimatedDuration']
    rmin_re = data['rmin_re']
    kp_18 = data['kp_18']
    kp_90 = data['kp_90']
    kp_135 = data['kp_135']
    kp_180 = data['kp_180']
    isEarthGB = data['isEarthGB']
    if data['impactList'] == None:
        impactList = None
    else:
        impactList = json.dumps(data['impactList'])
    link = data['link']

    insert_query = """
        INSERT INTO donki.wsaenlilsimulations_raw (
        simulationID,
        modelCompletionTime,
        au,
        cmeInputs,
        estimatedShockArrivalTime,
        estimatedDuration,
        rmin_re,
        kp_18,
        kp_90,
        kp_135,
        kp_180,
        isEarthGB,
        impactList,
        link
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    cursor.execute(insert_query, (simulationID, modelCompletionTime, au, cmeInputs, estimatedShockArrivalTime, estimatedDuration, rmin_re, kp_18, kp_90, kp_135, kp_180, isEarthGB, impactList, link))

def insert_earth_data(cursor, data):
    date = data['date']
    id = data['id']
    if data['resource'] == None:
        resource = None
    else:
        resource = json.dumps(data['resource'])
    service_version = data['service_version']
    url = data['url']

    insert_query = """
        INSERT INTO earth.earth_raw (
        date,
        id,
        resource,
        service_version,
        url 
        ) VALUES (%s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (date, id, resource, service_version, url))

def insert_earth_data(cursor, data):
    date = data['date']
    id = data['id']
    if data['resource'] == None:
        resource = None
    else:
        resource = json.dumps(data['resource'])
    service_version = data['service_version']
    url = data['url']

    insert_query = """
        INSERT INTO earth.earth_raw (
        date,
        id,
        resource,
        service_version,
        url 
        ) VALUES (%s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (date, id, resource, service_version, url))

def insert_epic_enhanced_data(cursor, data):
    identifier = data['identifier']
    caption = data['caption']
    image = data['image']
    version = data['version']
    if data['centroid_coordinates'] == None:
        centroid_coordinates = None
    else:
        centroid_coordinates = json.dumps(data['centroid_coordinates'])
    if data['dscovr_j2000_position'] == None:
        dscovr_j2000_position = None
    else:
        dscovr_j2000_position = json.dumps(data['dscovr_j2000_position'])
    if data['sun_j2000_position'] == None:
        sun_j2000_position = None
    else:
        sun_j2000_position = json.dumps(data['sun_j2000_position'])
    if data['lunar_j2000_position'] == None:
        lunar_j2000_position = None
    else:
        lunar_j2000_position = json.dumps(data['lunar_j2000_position'])
    if data['attitude_quaternions'] == None:
        attitude_quaternions = None
    else:
        attitude_quaternions = json.dumps(data['attitude_quaternions'])
    date = data['date']
    if data['coords'] == None:
        coords = None
    else:
        coords = json.dumps(data['coords'])

    insert_query = """
        INSERT INTO epic.epic_enhanced_raw (
        identifier,
        caption,
        image,
        version,
        centroid_coordinates,
        dscovr_j2000_position,
        lunar_j2000_position,
        sun_j2000_position,
        attitude_quaternions,
        date,
        coords
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (identifier, caption, image, version, centroid_coordinates, dscovr_j2000_position, lunar_j2000_position, sun_j2000_position, attitude_quaternions, date, coords))

def insert_epic_natural_data(cursor, data):
    identifier = data['identifier']
    caption = data['caption']
    image = data['image']
    version = data['version']
    if data['centroid_coordinates'] == None:
        centroid_coordinates = None
    else:
        centroid_coordinates = json.dumps(data['centroid_coordinates'])
    if data['dscovr_j2000_position'] == None:
        dscovr_j2000_position = None
    else:
        dscovr_j2000_position = json.dumps(data['dscovr_j2000_position'])
    if data['lunar_j2000_position'] == None:
        lunar_j2000_position = None
    else:
        lunar_j2000_position = json.dumps(data['lunar_j2000_position'])
    if data['sun_j2000_position'] == None:
        sun_j2000_position = None
    else:
        sun_j2000_position = json.dumps(data['sun_j2000_position'])
    if data['attitude_quaternions'] == None:
        attitude_quaternions = None
    else:
        attitude_quaternions = json.dumps(data['attitude_quaternions'])
    date = data['date']
    if data['coords'] == None:
        coords = None
    else:
        coords = json.dumps(data['coords'])

    insert_query = """
        INSERT INTO epic.epic_natural_raw (
        identifier,
        caption,
        image,
        version,
        centroid_coordinates,
        dscovr_j2000_position,
        lunar_j2000_position,
        sun_j2000_position,
        attitude_quaternions,
        date,
        coords
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    cursor.execute(insert_query, (identifier, caption, image, version, centroid_coordinates, dscovr_j2000_position, lunar_j2000_position, sun_j2000_position, attitude_quaternions, date, coords))

def insert_data(cursor):
    insert_query = """
        INSERT INTO donki.wsaenlilsimulations_impact_list (wsa_id, location, arrival_time, is_glancing_blow)
        SELECT id, value->>'location', value->>'arrivalTime', (value->>'isGlancingBlow')::BOOLEAN
        FROM donki.wsaenlilsimulations_raw,
            jsonb_array_elements(impactlist) as value;

        INSERT INTO donki.wsaenlilsimulations_cme_inputs (wsa_id, cmeid, speed, ipsList, latitude, time21_5, halfAngle, longitude, levelOfData, cmeStartTime, isMostAccurate)
        SELECT id, value->>'cmeid', value->>'speed', value->'ipsList', value->>'latitude', value->>'time21_5', value->>'halfAngle', value->>'longitude', value->>'levelOfData', value->>'cmeStartTime', value->>'isMostAccurate'
        FROM donki.wsaenlilsimulations_raw,
            jsonb_array_elements(cmeinputs) AS value;

        INSERT INTO donki.sep_linked_events (sep_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.sep_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.sep_instruments (sep_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.sep_raw,
            jsonb_array_elements(instruments) AS value;

        INSERT INTO donki.rbe_linked_events (rbe_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.rbe_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.rbe_instruments (rbe_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.rbe_raw,
            jsonb_array_elements(instruments) AS value;

        INSERT INTO donki.mpc_linked_events (mpc_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.mpc_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.mpc_instruments (mpc_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.mpc_raw,
            jsonb_array_elements(instruments) AS value;

        INSERT INTO donki.ips_instruments (ips_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.ips_raw,
            jsonb_array_elements(instruments) AS value;

        INSERT INTO donki.hss_linked_events (hss_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.hss_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.hss_instruments (hss_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.hss_raw,
            jsonb_array_elements(instruments) AS value;

        INSERT INTO donki.gst_linked_events (gst_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.gst_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.cme_linked_events (cme_id, activity_id)
        SELECT id, value->>'activityID'
        FROM donki.cme_raw,
            jsonb_array_elements(linkedevents) AS value;

        INSERT INTO donki.cme_cme_analyses (cme_id, link, note, type, speed, latitude, time21_5, enlil_list, half_angle, longitude, level_of_data, is_most_accurate)
        SELECT id, value->>'link', value->>'note', value->>'type', value->>'speed', value->>'latitude', value->>'time21_5', value->>'enlilList', value->>'halfAngle', value->>'longitude', value->>'levelOfData', value->>'isMostAccurate'
        FROM donki.cme_raw,
            jsonb_array_elements(cmeanalyses) AS value;

        INSERT INTO donki.gst_all_kp_index (gst_id, source, kp_index, observed_time)
        SELECT id, value->>'source', value->>'kpIndex', value->>'observedTime'
        FROM donki.gst_raw,
            jsonb_array_elements(allkpindex) AS value;

        INSERT INTO donki.cme_instruments (cme_id, display_name)
        SELECT id, value->>'displayName'
        FROM donki.cme_raw,
            jsonb_array_elements(instruments) AS value;
    """

    cursor.execute(insert_query)