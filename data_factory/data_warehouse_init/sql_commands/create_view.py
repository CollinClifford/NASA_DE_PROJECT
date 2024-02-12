def create_wsa_il_vw(cursor):
    create_query = """
        create or replace view donki.wsaenlilsimulations_impact_list_vw as
        select id
        , value->>'location' as location
        , value->>'arrivalTime' as arrival_time
        , value->>'isGlancingBlow' as is_glancing_blow
        from donki.wsaenlilsimulations_raw,
        jsonb_array_elements(impactlist) as value;
    """
    
    cursor.execute(create_query)

def create_wsa_cmei_vw(cursor):
    create_query = """
        create or replace view donki.wsaenlilsimulations_cme_inputs_vw as
        select id
        ,value->>'cmeid' as cmeid
        ,value->>'speed' as speed
        ,value->>'ipsList' as ipsList
        ,value->>'latitude' as latitude
        ,value->>'time21_5' as time21_5
        ,value->>'halfAngle' as halfAngle
        ,value->>'longitude' as longitude
        ,value->>'levelOfData' as levelOfData
        ,value->>'cmeStartTime' as cmeStartTime
        ,value->>'isMostAccurate' as isMostAccurate
        from donki.wsaenlilsimulations_raw,
        jsonb_array_elements(cmeinputs) as value;
    """

    cursor.execute(create_query)

def sep_le_vw(cursor):
    create_query = """
        create or replace view donki.sep_linked_events_vw as
        select id
        , value->>'activityID' as activity_id
        from donki.sep_raw,
        jsonb_array_elements(linkedevents) as value;
    """

    cursor.execute(create_query)

def sep_i_vw(cursor):
    create_query = """
        create or replace view donki.sep_instruments_vw as
        select id
        , value->>'displayName' as display_name
        from donki.sep_raw,
        jsonb_array_elements(instruments) as value;
    """

    cursor.execute(create_query)

def rbe_le_vw(cursor):
    create_query = """
        create or replace view donki.rbe_linked_events_vw as
        select id
        , value->>'activityID' as activity_id
        from donki.rbe_raw,
        jsonb_array_elements(linkedevents) as value;
    """

    cursor.execute(create_query)

def rbe_i_vw(cursor):
    create_query = """
        create or replace view donki.rbe_instruments_vw as
        select id
        , value->>'displayName' as display_name
        from donki.rbe_raw,
        jsonb_array_elements(instruments) as value;
    """

    cursor.execute(create_query)

def mpc_le_vw(cursor):
    create_query = """
        create or replace view donki.mpc_linked_events_vw as
        select id
        , value->>'activityID' as activity_id
        from donki.mpc_raw,
        jsonb_array_elements(linkedevents) as value;
    """

    cursor.execute(create_query)

def mpc_i_vw(cursor):
    create_query = """
        create or replace view donki.mpc_instruments_vw as
        select id
        , value->>'displayName' as display_name
        from donki.mpc_raw,
        jsonb_array_elements(instruments) as value;
    """

    cursor.execute(create_query)

def ip_i_vw(cursor):
    create_query = """
        create or replace view donki.ips_instruments_vw as
        select id,
        value->>'displayName' as display_name
        from donki.ips_raw,
        jsonb_array_elements(instruments) as value;
    """
    
    cursor.execute(create_query)

def hss_le_vw(cursor):
    create_query = """
        create or replace view donki.hss_linked_events_vw as
        select id
        ,value->>'activityID' as activity_id
        from donki.hss_raw,
        jsonb_array_elements(linkedevents) AS value;
    """

    cursor.execute(create_query)

def hss_i_vw(cursor):
    create_query = """
        create or replace view donki.hss_instruments_vw as
        select id
        ,value->>'displayName' as display_name
        from donki.hss_raw,
        jsonb_array_elements(instruments) AS value;
    """

    cursor.execute(create_query)

def gst_le_vw(cursor):
    create_query = """
        create or replace view donki.gst_linked_events_vw as
        select id
        , value->>'activityID' as activity_id
        from
        donki.gst_raw,
        jsonb_array_elements(linkedevents) AS value;
    """

    cursor.execute(create_query)

def cme_le_vw(cursor):
    create_query = """
        CREATE or replace VIEW donki.cme_linked_events_vw AS
        SELECT id, value->>'activityID' AS activity_id
        FROM donki.cme_raw,
            jsonb_array_elements(linkedevents) AS value;
    """

    cursor.execute(create_query)

def cme_a_vw(cursor):
    create_query = """
        create or REPLACE VIEW donki.cme_cme_analyses_vw AS
            SELECT id
            , value->>'link' AS link
            , value->>'note' as note
            , value->>'type' as type
            , value->>'speed' as speed
            , value->>'latitude' as latitude
            , value->>'time21_5' as time21_5
            , value->>'enlilList' as enlil_list
            , value->>'halfAngle' as half_angle
            , value->>'longitude' as longitude
            , value->>'levelOfData' as level_of_data
            , value->>'isMostAccurate' as is_most_accurate
            FROM donki.cme_raw,
                jsonb_array_elements(cmeanalyses) AS value;
    """

    cursor.execute(create_query)

def gst_kpi_vw(cursor):
    create_query = """
        CREATE OR REPLACE VIEW donki.gst_all_kp_index_vw AS
            SELECT id
            , value->>'source' AS source
            , value->>'kpIndex' as kp_index
            , value->>'observedTime' as observed_time
            FROM donki.gst_raw,
                jsonb_array_elements(allkpindex) AS value;
    """

    cursor.execute(create_query)

def cme_i_vw(cursor):
    create_query = """
        CREATE or replace VIEW donki.cme_instruments_vw AS
            SELECT id, value->>'displayName' AS display_name
            FROM donki.cme_raw,
                jsonb_array_elements(instruments) AS value;
    """

    cursor.execute(create_query)