import requests
import os
import json
import requests
from typing import Dict

def get_next_trip():
    # Intenta leer el archivo JSON donde se guarda el contador
    try:
        with open("counter.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o no tiene datos válidos, inicializa el contador en 0
        data = {"trip_counter": 0}
    
    # Incrementa el contador
    trip_counter = data["trip_counter"]
    data["trip_counter"] = trip_counter + 1
    
    # Escribe el nuevo valor del contador de vuelta al archivo JSON
    with open("counter.json", "w") as f:
        json.dump(data, f)
    
    # Retorna el valor actualizado del contador
    return trip_counter + 1


def post_request(url: str, data: Dict):
  response = requests.post(url, json=data)
  print(f"Response status code: {response.status_code}")
  print(f"Response content: {response.json}")
  assert  response.status_code in [200, 201]
  return response.json()
