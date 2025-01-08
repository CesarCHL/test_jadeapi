# test_api.py
import os, time
from logic import post_request, update_trip
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture
def plant():
    class Plant:
        def __init__(self, name):
            self.name = name

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

        def get_staging_event_data(self, screen_line, sensores):
            {
                "factoryPlant": self.name,
                "screenLine": screen_line,
                "sensors": [{"number": i + 1, "active": 0} for i in range(sensores)]
            }

    return Plant

def test_addTrip_Planning():
    url = os.getenv("API_tripPlanning")
    data = {
        "trip": 31,
        "planta": "PTA 1 (CD)",
        "fecha": "2024-11-11"
    }
    post_request(url, data)

@pytest.mark.parametrize("plant_instance", [
    ("PTA 1 (CD)", 12), # 12 sensores
    ("Plant 4", 7), # 7 sensores
    ("PTA 5 (CD)", 15)  # 15 sensores
])
@pytest.mark.parametrize("tipoCarga", ["Carga regular", "Carga lateral"])
@pytest.mark.parametrize("tipoCaja", ["Caja seca", "Plataforma"])
@pytest.mark.parametrize("tipoTurno", ["Exportación", "Grupo Comercial", "Nacional", "Recibo mercancía"])

def test_addTrip(plant, plant_instance, tipoCarga, tipoCaja, tipoTurno):
    plant_name, sensores = plant_instance
    plant_obj = plant(plant_name, plant_instance[1])
    data = plant_obj.create_trip_data(update_trip(), tipo_carga=tipoCarga, tipo_caja=tipoCaja, tipo_turno=tipoTurno)
    post_request(url, data)
    expected_plants = ["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"]
    assert data["planta"] in expected_plants, f"Unexpected value: {data['planta']}"

def test_stagingEvent(plant):
    plant_obj = plant("PTA 1 (CD)")
    url = os.getenv("API_stagingEvent")
    data = plant_obj.get_staging_event_data(screen_line=1, sensores=15)
    try:
        post_request(url, data) 
        print(f"Trip sent: {data['factoryPlant']}")
        time.sleep(10)
    except KeyboardInterrupt:
        print("Test interrupted")
        exit(0)

if __name__ == "__main__":
    pytest.main()
