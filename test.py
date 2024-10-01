from src import extract, transform, load

def test_etl():
    try:
        # Simulate extract step
        print("Starting data extraction...")
        flight_data = extract.get_flight_data()
        print("Data extraction completed.")

        # Simulate transform step
        print("Starting data transformation...")
        transformed_data = transform.process_flight_data(flight_data)
        print("Data transformation completed.")

        # Simulate load step
        print("Starting data load...")
        load.save_flight_data(transformed_data)
        print("Data load completed.")
        
    except Exception as e:
        print(f"ETL process failed: {e}")

if __name__ == "__main__":
    test_etl()
