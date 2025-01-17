import requests
import json
import requests
from typing import Dict

import json

# Update trip
def update_trip():
    # Intenta leer el archivo JSON donde se guarda el contador
    try:
        with open("counter.json", "r") as f:
            data = json.load(f) #Store JSON value in data
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"trip_counter": 0}
    
    trip_counter = data["trip_counter"]
    data["trip_counter"] = trip_counter + 1

    # Update new value to JSON
    with open("counter.json", "w") as a:
        json.dump(data, a)

    return trip_counter + 1


#Server status response
def post_request(url: str, data: Dict):
    response = requests.post(url, json=data)
    print(f"Response status code: {response.status_code}")
    assert  response.status_code in [200, 201]
    return response.json()

    