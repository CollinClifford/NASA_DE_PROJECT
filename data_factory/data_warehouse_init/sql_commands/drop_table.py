def dt_apod(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS apod.apod_raw;
    """
    
    cursor.execute(drop_table_query)

def dt_cme(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.cme_raw; 
    """

    cursor.execute(drop_table_query)

def dt_cme_analysis(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.cme_analysis_raw;
    """

    cursor.execute(drop_table_query)

def dt_gst(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.gst_raw;
    """

    cursor.execute(drop_table_query)

def dt_hss(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.hss_raw;
    """

    cursor.execute(drop_table_query)

def dt_ips(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.ips_raw;
    """

    cursor.execute(drop_table_query)

def dt_mpc(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.mpc_raw;
    """

    cursor.execute(drop_table_query)

def dt_notifications(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.notifications_raw;
    """

    cursor.execute(drop_table_query)

def dt_rbe(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.rbe_raw;
    """

    cursor.execute(drop_table_query)

def dt_sep(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.sep_raw;
    """

    cursor.execute(drop_table_query)

def dt_wsaenlilsimulations(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS donki.wsaenlilsimulations_raw;
    """

    cursor.execute(drop_table_query)

def dt_earth(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS earth.earth_raw;
    """

    cursor.execute(drop_table_query)

def dt_epic_enhanced(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS epic.epic_enhanced_raw;
    """

    cursor.execute(drop_table_query)

def dt_epic_natural(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS epic.epic_natural_raw;
    """

    cursor.execute(drop_table_query)

def dt_mars_rover_photos_curiosity(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS mars_rover_photos.curiosity_raw;
    """

    cursor.execute(drop_table_query)

def dt_mars_rover_photos_opportunity(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS mars_rover_photos.opportunity_raw;
    """

    cursor.execute(drop_table_query)

def dt_mars_rover_photos_perseverance(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS mars_rover_photos.perseverance_raw;
    """

    cursor.execute(drop_table_query)

def dt_mars_rover_photos_spirit(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS mars_rover_photos.spirit_raw;
    """

    cursor.execute(drop_table_query)

def dt_neows(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS neows.neows_raw;
    """

    cursor.execute(drop_table_query)