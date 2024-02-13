def drop_schema(cursor):
    drop_query = """
        DROP SCHEMA IF EXISTS apod;
        DROP SCHEMA IF EXISTS donki;
        DROP SCHEMA IF EXISTS earth;
        DROP SCHEMA IF EXISTS epic;
        DROP SCHEMA IF EXISTS mars_rover_photo;
        DROP SCHEMA IF EXISTS neows;
    """

    cursor.execute(drop_query)