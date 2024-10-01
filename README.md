# Project: Air New Zealand Live Flight ETL 

This project implements an ETL pipeline that scrapes live flight data from Radarbox, processes it, and stores it in a PostgreSQL database. The pipeline is orchestrated using Apache Airflow, allowing for scheduled execution and task management.


## Technologies Used
* Apache Airflow: For orchestrating the ETL process.
* Python: For scripting the extraction, transformation, and loading of data.
* PostgreSQL: For storing the flight data.
* Requests: For making HTTP requests to scrape live flight data.
## Database Overview
The database stores flight information, including attributes like flight number, latitude, longitude, altitude, aircraft type, ground speed, origin, destination, and airline. Below is an example of the data stored in the flight_data table:

!

## Airflow DAG Overview

The ETL process is managed by Apache Airflow through a Directed Acyclic Graph (DAG). Below is a visual representation of the DAG, illustrating the sequence of tasks involved in the ETL process:

!

### DAG Tasks

1. **extract_flight_data**: 
   - This task retrieves live flight data from Radarbox using HTTP requests.
   
2. **transform_flight_data**: 
   - This task processes the extracted data to ensure it is clean, consistent, and ready for loading.
   
3. **load_flight_data**: 
   - This task loads the transformed data into a PostgreSQL database for storag

### Execution Flow

The tasks are executed in the following order:
- The **extract_flight_data** task runs first.
- Once data extraction is complete, the **transform_flight_data** task executes.
- Finally, the **load_flight_data** task loads the processed data into the database.