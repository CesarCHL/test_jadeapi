# test_api.py
import os
import pytest
from logic import get_next_trip, post_request
from dotenv import load_dotenv

load_dotenv()

#Post addTripPlanning
def test_addTrip_Planning():
    url = os.getenv("API_tripPlanning")
    data = { 
        "trip": 31,
        "planta": "PTA 1 (CD)", 
        "fecha": "2024-11-11"
    }
    post_request(url, data)

#Post addTrip
def test_addTrip():
    url = os.getenv("API_addTrip")
    data = {
        "trip": get_next_trip(),
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

#Post steagingEvent
def test_stagingEvent():
    url = os.getenv("API_stagingEvent")
    data = {
        "factoryPlant": "Pta 1 (CD)",
        "screenLine": 1,
        "sensors": [
           {"number": 1, "active": 0},
           {"number": 2, "active": 0},
           {"number": 3, "active": 0},
           {"number": 4, "active": 0},
           {"number": 5, "active": 0},
           {"number": 6, "active": 0},
           {"number": 7, "active": 0},
           {"number": 8, "active": 0},
           {"number": 9, "active": 1},
           {"number": 10, "active": 0},
           {"number": 11, "active": 0},
           {"number": 12, "active": 0},
           {"number": 13, "active": 0},
           {"number": 14, "active": 0},
           {"number": 15, "active": 0}
        ]
    }
    post_request(url, data)
