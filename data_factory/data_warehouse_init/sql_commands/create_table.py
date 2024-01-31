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

def ct_neows(cursor):
    create_table_query = """
    CREATE TABLE neows.neows_raw (
    id SERIAL PRIMARY KEY,
    date date UNIQUE,
    objects JSONB
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
    latitude double,
    longitude double,
    halfAngle double,
    speed double,
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