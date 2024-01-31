def ct_apod(cursor):
    create_table_query = """
    CREATE TABLE apod.apod_raw (
    id SERIAL PRIMARY KEY,
    service_version text,
    media_type text,
    hdurl text,
    title text,
    copyright text,
    url text,
    date date UNIQUE,
    explanation text,
    thumbnail_url text
    )
    """
    
    cursor.execute(create_table_query)

def ct_cme(cursor):
    create_table_query = """
    CREATE TABLE donki.cme_raw (
    id SERIAL PRIMARY KEY,
    activityID text UNIQUE,
    catalog text,
    startTime date,
    sourceLocation text,
    activeRegionNum text,
    link text,
    note text,
    instruments JSONB,
    cmeAnalyses JSONB,
    linkedEvents text
    )
    """

    cursor.execute(create_table_query)

def ct_cme_analysis(cursor):
    create_table_query = """
    CREATE TABLE donki.cme_analysis_raw (
    id SERIAL PRIMARY KEY,
    time21_5 date UNIQUE,
    latitude float,
    longitude float,
    halfAngle float,
    speed float,
    type text,
    isMostAccurate boolean,
    associatedCMEID text,
    note text,
    catalog text,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_gst(cursor):
    create_table_query = """
    CREATE TABLE donki.gst_raw (
    id SERIAL PRIMARY KEY,
    gstID text UNIQUE,
    startTime date,
    allKpIndex JSONB,
    linkedEvents JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_hss(cursor):
    create_table_query = """
    CREATE TABLE donki.hss_raw (
    id SERIAL PRIMARY KEY,
    hssID text UNIQUE,
    eventTime date,
    instruments JSONB,
    linkedEvents JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_ips(cursor):
    create_table_query = """
    CREATE TABLE donki.ips_raw (
    id SERIAL PRIMARY KEY,
    catalog text,
    activityID text UNIQUE,
    location text,
    eventTime date,
    link text,
    instruments JSONB
    )
    """

    cursor.execute(create_table_query)

def ct_mpc(cursor):
    create_table_query = """
    CREATE TABLE donki.mpc_raw (
    id SERIAL PRIMARY KEY,
    mpcID text UNIQUE,
    eventTime date,
    instruments JSONB,
    linkedEvents JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_notifications(cursor):
    create_table_query = """
    CREATE TABLE donki.notifications_raw (
    id SERIAL PRIMARY KEY,
    messageType text,
    messageID text UNIQUE,
    messageURL text,
    messageIssueTime date,
    messageBody text
    )
    """

    cursor.execute(create_table_query)

def ct_rbe(cursor):
    create_table_query = """
    CREATE TABLE donki.rbe_raw (
    id SERIAL PRIMARY KEY,
    rbeID text UNIQUE,
    eventTime date,
    instruments JSONB,
    linkedEvents JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_sep(cursor):
    create_table_query = """
    CREATE TABLE donki.sep_raw (
    id SERIAL PRIMARY KEY,
    sepID text UNIQUE,
    eventTime date,
    instruments JSONB,
    linkedEvents JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_wsaenlilsimulations(cursor):
    create_table_query = """
    CREATE TABLE donki.wsaenlilsimulations_raw (
    id SERIAL PRIMARY KEY,
    simulationID text UNIQUE,
    modelCompletionTime date,
    au float,
    cmeInputs JSONB,
    estimatedShockArrivalTime text,
    estimatedDuration text,
    rmin_re text,
    kp_18 text,
    kp_90 text,
    kp_135 text,
    kp_180 text,
    isEarthGB boolean,
    impactList JSONB,
    link text
    )
    """

    cursor.execute(create_table_query)

def ct_earth(cursor):
    create_table_query = """
    CREATE TABLE earth.earth_raw (
    date date,
    id text UNIQUE,
    resure JSONB,
    service_version text,
    url text
    )
    """

    cursor.execute(create_table_query)

def ct_epic_enhanced(cursor):
    create_table_query = """
    CREATE TABLE epic.epic_enhanced_raw (
    id SERIAL PRIMARY KEY,
    identifier text UNIQUE,
    caption text,
    image text,
    version text,
    centroid_coordinates JSONB,
    dscovr_j2000_position JSONB,
    lunar_j2000_position JSONB,
    sun_j2000_position JSONB,
    attitude_quaternions JSONB,
    date date,
    coords JSONB
    )
    """

    cursor.execute(create_table_query)

def ct_epic_natural(cursor):
    create_table_query = """
    CREATE TABLE epic.epic_natural_raw (
    id SERIAL PRIMARY KEY,
    identifier text UNIQUE,
    caption text,
    image text,
    version text,
    centroid_coordinates JSONB,
    dscovr_j2000_position JSONB,
    lunar_j2000_position JSONB,
    sun_j2000_position JSONB,
    attitude_quaternions JSONB,
    date date,
    coords JSONB
    )
    """

    cursor.execute(create_table_query)

def ct_mars_rover_photos_curiosity(cursor):
    create_table_query = """
    CREATE TABLE mars_rover_photos.curiosity_raw (
    id SERIAL PRIMARY KEY
    )
    """

    cursor.execute(create_table_query)

def ct_mars_rover_photos_opportunity(cursor):
    create_table_query = """
    CREATE TABLE mars_rover_photos.opportunity_raw (
    id SERIAL PRIMARY KEY
    )
    """

    cursor.execute(create_table_query)

def ct_mars_rover_photos_perseverance(cursor):
    create_table_query = """
    CREATE TABLE mars_rover_photos.perseverance_raw (
    id SERIAL PRIMARY KEY
    )
    """

    cursor.execute(create_table_query)

def ct_mars_rover_photos_spirit(cursor):
    create_table_query = """
    CREATE TABLE mars_rover_photos.spirit_raw (
    id SERIAL PRIMARY KEY
    )
    """

    cursor.execute(create_table_query)

def ct_neows(cursor):
    create_table_query = """
    CREATE TABLE neows.neows_raw (
    id SERIAL PRIMARY KEY,
    date date,
    objects JSONB
    )
    """

    cursor.execute(create_table_query)