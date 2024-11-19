import requests
import random
import pytest
from dotenv import load_dotenv
from typing import List, Dict
import os

load_dotenv()

def post_request(url: str, data: Dict):
  response = requests.post(url, json=data)
  print(f"Response status code: {response.status_code}")
  print(f"Response content: {response.json}")
  assert  response.status_code in [200, 201]
  return response.json()

# POST addTripsPlanning
def test_addTrip_Planning():
    url = os.getenv("API_tripPlanning")
    data = { 
        "trip": 31,
        "planta": "PTA 1 (CD)", 
        "fecha": "2024-11-11"
    }
    post_request(url, data)

# POST addTrips
def test_addTrip():
    url = os.getenv("API_addTrip")
    data = {
    "trip": "0987",
    "planta": "PTA 1 (CD)",
    "tipoCarga": "CARGA REGULAR",
    "tipoCaja":"CAJA SECA",
    "areaCarga": "EXPLANADA/BODEGA",
    "turno": "2",
    "tipoTurno":"GRUPO_COM",
    "carrier": "Carrier 2",
    "driver": "Driver 2"
}
    post_request(url, data)

# POST stagingEvent
def test_stagingEvent():
    url = os.getenv("API_stagingEvent")
    data = {
        "factoryPlant": "Pta 1 (CD)",
        "screenLine": 1,
        "sensors": [
           {
             "number": 1,
             "active": 0
           },
           {
             "number": 2,
             "active": 0
           },
           {
             "number": 3,
             "active": 0
           },
           {
             "number": 4,
             "active": 0
           },
           {
             "number": 5,
             "active": 0
           },
           {
             "number": 6,
             "active": 0
           },
           {
             "number": 7,
             "active": 0
           },
           {
             "number": 8,
             "active": 0
           },
           {
             "number": 9,
             "active": 1
           },
           {
             "number": 10,
             "active": 0
           },
           {
             "number": 11,
             "active": 0
           },
           {
             "number": 12,
             "active": 0
           },
           {
             "number": 13,
             "active": 0
           },
           {
             "number": 14,
             "active": 0
           },
           {
             "number": 15,
             "active": 0
           }
        ]
    }
    post_request(url, data)