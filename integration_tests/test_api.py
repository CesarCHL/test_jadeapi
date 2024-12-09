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
    
    
class Plant:
    def __init__(self, name, area_carga="EXPLANADA/BODEGA"):
        self.name = name
        self.area_carga = area_carga

    def create_trip_data(self, trip, tipo_carga, tipo_caja, tipo_turno):
        return {
            "trip": trip,
            "planta": self.name,
            "tipoCarga": tipo_carga,
            "tipoCaja": tipo_caja,
            "areaCarga": self.area_carga,
            "turno": "2",
            "tipoTurno": tipo_turno,
            "carrier": "Carrier 2",
            "driver": "Driver 2",
        }

@pytest.mark.parametrize("plant", [
    Plant("PTA 1 (CD)"),
    Plant("Plant 4"),
    Plant("PTA 5 (CD)")
])
@pytest.mark.parametrize("tipoCarga", ["Carga regular", "Carga lateral"])   
@pytest.mark.parametrize("tipoCaja", ["Caja seca", "Plataforma"])
@pytest.mark.parametrize("tipoTurno", ["Exportación", "Grupo Comercial", "Nacional", "Recibo mercancía"])

def test_addTrip(plant, tipoCarga, tipoCaja, tipoTurno):
    url = os.getenv("API_addTrip")
    data = plant.create_trip_data(update_trip(), tipo_carga=tipoCarga, tipo_caja=tipoCaja, tipo_turno=tipoTurno)
    post_request(url, data)
    expected_plants = ["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"]
    assert data["planta"] in expected_plants, f"Unexpected value: {data['planta']}"


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

    