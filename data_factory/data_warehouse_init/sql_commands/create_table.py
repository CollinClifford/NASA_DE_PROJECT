def create_table(cursor):
    create_query = """
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
    );
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
        linkedEvents JSONB
    );
    CREATE TABLE donki.cme_analysis_raw (
        id SERIAL PRIMARY KEY,
        time21_5 date,
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
    );
    CREATE TABLE donki.gst_raw (
        id SERIAL PRIMARY KEY,
        gstID text UNIQUE,
        startTime date,
        allKpIndex JSONB,
        linkedEvents JSONB,
        link text
    );
    CREATE TABLE donki.hss_raw (
        id SERIAL PRIMARY KEY,
        hssID text UNIQUE,
        eventTime date,
        instruments JSONB,
        linkedEvents JSONB,
        link text
    );
    CREATE TABLE donki.ips_raw (
        id SERIAL PRIMARY KEY,
        catalog text,
        activityID text UNIQUE,
        location text,
        eventTime date,
        link text,
        instruments JSONB
    );
    CREATE TABLE donki.mpc_raw (
        id SERIAL PRIMARY KEY,
        mpcID text UNIQUE,
        eventTime date,
        instruments JSONB,
        linkedEvents JSONB,
        link text
    );
    CREATE TABLE donki.notifications_raw (
        id SERIAL PRIMARY KEY,
        messageType text,
        messageID text UNIQUE,
        messageURL text,
        messageIssueTime date,
        messageBody text
    );
    CREATE TABLE donki.rbe_raw (
        id SERIAL PRIMARY KEY,
        rbeID text UNIQUE,
        eventTime date,
        instruments JSONB,
        linkedEvents JSONB,
        link text
    );
    CREATE TABLE donki.sep_raw (
        id SERIAL PRIMARY KEY,
        sepID text UNIQUE,
        eventTime date,
        instruments JSONB,
        linkedEvents JSONB,
        link text
    );
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
    );
    CREATE TABLE earth.earth_raw (
        date date,
        id text UNIQUE,
        resource JSONB,
        service_version text,
        url text
    );
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
    );
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
    );
    CREATE TABLE mars_rover_photos.curiosity_raw (
        id SERIAL PRIMARY KEY
    );
    CREATE TABLE mars_rover_photos.opportunity_raw (
        id SERIAL PRIMARY KEY
    );
    CREATE TABLE mars_rover_photos.perseverance_raw (
        id SERIAL PRIMARY KEY
    );
    CREATE TABLE mars_rover_photos.spirit_raw (
        id SERIAL PRIMARY KEY
    );
    CREATE TABLE neows.neows_raw (
        id SERIAL PRIMARY KEY,
        date date,
        objects JSONB
    );
    CREATE TABLE donki.wsaenlilsimulations_impact_list (
        id SERIAL PRIMARY KEY,
        wsa_id INTEGER,
        location TEXT,
        arrival_time TEXT,
        is_glancing_blow BOOLEAN,
        FOREIGN KEY (wsa_id) REFERENCES donki.wsaenlilsimulations_raw(id)
    );
    CREATE TABLE donki.wsaenlilsimulations_cme_inputs (
        id SERIAL PRIMARY KEY,
        wsa_id INTEGER,
        cmeid TEXT,
        speed TEXT,
        ipsList TEXT,
        latitude TEXT,
        time21_5 TEXT,
        halfAngle TEXT,
        longitude TEXT,
        levelOfData TEXT,
        cmeStartTime TEXT,
        isMostAccurate TEXT,
        FOREIGN KEY (wsa_id) REFERENCES donki.wsaenlilsimulations_raw(id)
    );
    CREATE TABLE donki.sep_linked_events (
        id SERIAL PRIMARY KEY,
        sep_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (sep_id) REFERENCES donki.sep_raw(id)
    );
    CREATE TABLE donki.sep_instruments (
        id SERIAL PRIMARY KEY,
        sep_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (sep_id) REFERENCES donki.sep_raw(id)
    );
    CREATE TABLE donki.rbe_linked_events (
        id SERIAL PRIMARY KEY,
        rbe_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (rbe_id) REFERENCES donki.rbe_raw(id)
    );
    CREATE TABLE donki.rbe_instruments (
        id SERIAL PRIMARY KEY,
        rbe_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (rbe_id) REFERENCES donki.rbe_raw(id)
    );
    CREATE TABLE donki.mpc_linked_events (
        id SERIAL PRIMARY KEY,
        mpc_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (mpc_id) REFERENCES donki.mpc_raw(id)
    );
    CREATE TABLE donki.mpc_instruments (
        id SERIAL PRIMARY KEY,
        mpc_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (mpc_id) REFERENCES donki.mpc_raw(id)
    );
    CREATE TABLE donki.ips_instruments (
        id SERIAL PRIMARY KEY,
        ips_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (ips_id) REFERENCES donki.ips_raw(id)
    );
    CREATE TABLE donki.hss_linked_events (
        id SERIAL PRIMARY KEY,
        hss_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (hss_id) REFERENCES donki.hss_raw(id)
    );
    CREATE TABLE donki.hss_instruments (
        id SERIAL PRIMARY KEY,
        hss_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (hss_id) REFERENCES donki.hss_raw(id)
    );
    CREATE TABLE donki.gst_linked_events (
        id SERIAL PRIMARY KEY,
        gst_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (gst_id) REFERENCES donki.gst_raw(id)
    );
    CREATE TABLE donki.cme_linked_events (
        id SERIAL PRIMARY KEY,
        cme_id INTEGER,
        activity_id TEXT,
        FOREIGN KEY (cme_id) REFERENCES donki.cme_raw(id)
    );
    CREATE TABLE donki.cme_cme_analyses (
        id SERIAL PRIMARY KEY,
        cme_id INTEGER,
        link TEXT,
        note TEXT,
        type TEXT,
        speed TEXT,
        latitude TEXT,
        time21_5 TEXT,
        enlil_list TEXT,
        half_angle TEXT,
        longitude TEXT,
        level_of_data TEXT,
        is_most_accurate TEXT,
        FOREIGN KEY (cme_id) REFERENCES donki.cme_raw(id)
    );
    CREATE TABLE donki.gst_all_kp_index (
        id SERIAL PRIMARY KEY,
        gst_id INTEGER,
        source TEXT,
        kp_index TEXT,
        observed_time TEXT,
        FOREIGN KEY (gst_id) REFERENCES donki.gst_raw(id)
    );
    CREATE TABLE donki.cme_instruments (
        id SERIAL PRIMARY KEY,
        cme_id INTEGER,
        display_name TEXT,
        FOREIGN KEY (cme_id) REFERENCES donki.cme_raw(id)
    );
    """
    
    cursor.execute(create_query)


# def ct_apod(cursor):
#     create_table_query = """
#     CREATE TABLE apod.apod_raw (
#     id SERIAL PRIMARY KEY,
#     service_version text,
#     media_type text,
#     hdurl text,
#     title text,
#     copyright text,
#     url text,
#     date date UNIQUE,
#     explanation text,
#     thumbnail_url text
#     )
#     """
    
#     cursor.execute(create_table_query)

# def ct_cme(cursor):
#     create_table_query = """
#     CREATE TABLE donki.cme_raw (
#     id SERIAL PRIMARY KEY,
#     activityID text UNIQUE,
#     catalog text,
#     startTime date,
#     sourceLocation text,
#     activeRegionNum text,
#     link text,
#     note text,
#     instruments JSONB,
#     cmeAnalyses JSONB,
#     linkedEvents JSONB
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_cme_analysis(cursor):
#     create_table_query = """
#     CREATE TABLE donki.cme_analysis_raw (
#     id SERIAL PRIMARY KEY,
#     time21_5 date,
#     latitude float,
#     longitude float,
#     halfAngle float,
#     speed float,
#     type text,
#     isMostAccurate boolean,
#     associatedCMEID text,
#     note text,
#     catalog text,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_gst(cursor):
#     create_table_query = """
#     CREATE TABLE donki.gst_raw (
#     id SERIAL PRIMARY KEY,
#     gstID text UNIQUE,
#     startTime date,
#     allKpIndex JSONB,
#     linkedEvents JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_hss(cursor):
#     create_table_query = """
#     CREATE TABLE donki.hss_raw (
#     id SERIAL PRIMARY KEY,
#     hssID text UNIQUE,
#     eventTime date,
#     instruments JSONB,
#     linkedEvents JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_ips(cursor):
#     create_table_query = """
#     CREATE TABLE donki.ips_raw (
#     id SERIAL PRIMARY KEY,
#     catalog text,
#     activityID text UNIQUE,
#     location text,
#     eventTime date,
#     link text,
#     instruments JSONB
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_mpc(cursor):
#     create_table_query = """
#     CREATE TABLE donki.mpc_raw (
#     id SERIAL PRIMARY KEY,
#     mpcID text UNIQUE,
#     eventTime date,
#     instruments JSONB,
#     linkedEvents JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_notifications(cursor):
#     create_table_query = """
#     CREATE TABLE donki.notifications_raw (
#     id SERIAL PRIMARY KEY,
#     messageType text,
#     messageID text UNIQUE,
#     messageURL text,
#     messageIssueTime date,
#     messageBody text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_rbe(cursor):
#     create_table_query = """
#     CREATE TABLE donki.rbe_raw (
#     id SERIAL PRIMARY KEY,
#     rbeID text UNIQUE,
#     eventTime date,
#     instruments JSONB,
#     linkedEvents JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_sep(cursor):
#     create_table_query = """
#     CREATE TABLE donki.sep_raw (
#     id SERIAL PRIMARY KEY,
#     sepID text UNIQUE,
#     eventTime date,
#     instruments JSONB,
#     linkedEvents JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_wsaenlilsimulations(cursor):
#     create_table_query = """
#     CREATE TABLE donki.wsaenlilsimulations_raw (
#     id SERIAL PRIMARY KEY,
#     simulationID text UNIQUE,
#     modelCompletionTime date,
#     au float,
#     cmeInputs JSONB,
#     estimatedShockArrivalTime text,
#     estimatedDuration text,
#     rmin_re text,
#     kp_18 text,
#     kp_90 text,
#     kp_135 text,
#     kp_180 text,
#     isEarthGB boolean,
#     impactList JSONB,
#     link text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_earth(cursor):
#     create_table_query = """
#     CREATE TABLE earth.earth_raw (
#     date date,
#     id text UNIQUE,
#     resource JSONB,
#     service_version text,
#     url text
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_epic_enhanced(cursor):
#     create_table_query = """
#     CREATE TABLE epic.epic_enhanced_raw (
#     id SERIAL PRIMARY KEY,
#     identifier text UNIQUE,
#     caption text,
#     image text,
#     version text,
#     centroid_coordinates JSONB,
#     dscovr_j2000_position JSONB,
#     lunar_j2000_position JSONB,
#     sun_j2000_position JSONB,
#     attitude_quaternions JSONB,
#     date date,
#     coords JSONB
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_epic_natural(cursor):
#     create_table_query = """
#     CREATE TABLE epic.epic_natural_raw (
#     id SERIAL PRIMARY KEY,
#     identifier text UNIQUE,
#     caption text,
#     image text,
#     version text,
#     centroid_coordinates JSONB,
#     dscovr_j2000_position JSONB,
#     lunar_j2000_position JSONB,
#     sun_j2000_position JSONB,
#     attitude_quaternions JSONB,
#     date date,
#     coords JSONB
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_mars_rover_photos_curiosity(cursor):
#     create_table_query = """
#     CREATE TABLE mars_rover_photos.curiosity_raw (
#     id SERIAL PRIMARY KEY
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_mars_rover_photos_opportunity(cursor):
#     create_table_query = """
#     CREATE TABLE mars_rover_photos.opportunity_raw (
#     id SERIAL PRIMARY KEY
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_mars_rover_photos_perseverance(cursor):
#     create_table_query = """
#     CREATE TABLE mars_rover_photos.perseverance_raw (
#     id SERIAL PRIMARY KEY
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_mars_rover_photos_spirit(cursor):
#     create_table_query = """
#     CREATE TABLE mars_rover_photos.spirit_raw (
#     id SERIAL PRIMARY KEY
#     )
#     """

#     cursor.execute(create_table_query)

# def ct_neows(cursor):
#     create_table_query = """
#     CREATE TABLE neows.neows_raw (
#     id SERIAL PRIMARY KEY,
#     date date,
#     objects JSONB
#     )
#     """

#     cursor.execute(create_table_query)