import psycopg2

def save_flight_data(flight_list):
    conn_string = "postgresql://xremsutr:vekmtfizzbvoojnlrsbd@alpha.mkdb.sh:5432/veausmtf"
    
    # connect to database
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # delete data
    cursor.execute("TRUNCATE TABLE flight_data;")

    # insert the flight data
    for flight in flight_list:
        cursor.execute("""
            INSERT INTO flight_data (flight_number, latitude, longitude, altitude, aircraft_type, ground_speed, origin, destination, airline)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (flight["flight_number"], flight["latitude"], flight["longitude"], flight["altitude"], flight["aircraft_type"], flight["ground_speed"], flight["origin"], flight["destination"], flight["airline"]))
    
    conn.commit()
    cursor.close()
    conn.close()
