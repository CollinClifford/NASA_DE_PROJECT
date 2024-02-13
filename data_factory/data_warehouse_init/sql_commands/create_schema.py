def create_schema(cursor):
    create_query = """
        CREATE SCHEMA IF NOT EXISTS apod;
        CREATE SCHEMA IF NOT EXISTS donki;
        CREATE SCHEMA IF NOT EXISTS earth;
        CREATE SCHEMA IF NOT EXISTS epic;
        CREATE SCHEMA IF NOT EXISTS mars_rover_photo;
        CREATE SCHEMA IF NOT EXISTS neows;
    """

    cursor.execute(create_query)