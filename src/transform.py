def process_flight_data(data):
    flight_list = []

    for flight_id, flight_data in data[0].items():
        if flight_data:
            flight = {
                "flight_number": flight_data[0] if flight_data[0] != '' else None,
                "latitude": flight_data[1] if flight_data[1] != '' else None,
                "longitude": flight_data[2] if flight_data[2] != '' else None,
                "altitude": flight_data[4] if flight_data[4] != '' else None,
                "aircraft_type": flight_data[5] if flight_data[5] != '' else None,
                "ground_speed": flight_data[6] if flight_data[6] != '' else None,
                "origin": flight_data[10] if flight_data[10] != '' else None,
                "destination": flight_data[11] if flight_data[11] != '' else None,
                "airline": flight_data[12] if flight_data[12] != '' else None,
            }
            flight_list.append(flight)

    return flight_list
