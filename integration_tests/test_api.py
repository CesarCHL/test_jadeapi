# test_api.py
import os
from integration_tests.logic import   post_request, update_trip
from dotenv import load_dotenv
import random
import pytest

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
"""
    This test checks the functionality of adding a trip with various parameters.
    It uses parameterization to send different combinations of 'planta', 'tipoCarga',
    'tipoCaja', and 'tipoTurno' to the API.
"""

@pytest.mark.parametrize("planta", ["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"])
@pytest.mark.parametrize("tipoCarga", ["Carga regular", "Carga lateral"])   
@pytest.mark.parametrize("tipoCaja", ["Caja seca", "Plataforma"])
@pytest.mark.parametrize("tipoTurno", ["Exportación", "Grupo Comercial", "Nacional", "Recibo mercancía"])

#Post addTrip
def test_addTrip():
    url = os.getenv("API_addTrip")
    data = { 
        "trip": update_trip(),
        "planta": random.choice(["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"] ),
        "tipoCarga": random.choice(["Carga regular", "Carga lateral"]),
        "tipoCaja": random.choice(["Caja seca", "Plataforma"]),
        "areaCarga": "EXPLANADA/BODEGA",
        "turno": "2",
        "tipoTurno": random.choice(["Exportación", "Grupo Comercial", "Nacional", "Recibo mercancía"]),
        "carrier": "Carrier 2",
        "driver": "Driver 2"
    }
    post_request(url, data)
    expected_values = ["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"]
    assert data in expected_values, f"Unexpected value: {data}"


#Post stagingEvent
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
           {"number": 9, "active": 0},
           {"number": 10, "active": 0},
           {"number": 11, "active": 0},
           {"number": 12, "active": 0},
           {"number": 13, "active": 0},
           {"number": 14, "active": 0},
           {"number": 15, "active": 0}
        ]
    }
    post_request(url, data)

if __name__ == "__main__":
    test_addTrip()