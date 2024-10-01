import time
import requests
from config.settings import HEADERS, BASE_URL

def get_current_timestamp():
    return int(time.time() * 1000) - 300000

def get_flight_data():
    url = BASE_URL.format(timestamp=get_current_timestamp())
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
