import requests, logging, datetime, time, os
from logic import update_trip, post_request
from itertools import product
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

def add_trip_planning(planta):
    url = os.getenv("API_tripPlanning")
    data = {
        "trip": update_trip,
        "planta": planta,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d")
    }
    response = post_request(url, data=data)
    return response.json()

def add_trip(trip_id, planta, tipo_carga, tipo_caja, area_carga):
    url = os.getenv("API_addTrip")
    data = {
        "trip": trip_id,
        "planta": planta,
        "tipoCarga": tipo_carga,
        "tipoCaja": tipo_caja,
        "areaCarga": area_carga,
        "turno": "2",
        "tipoTurno": "GRUPO_COM",
        "carrier": "Carrier 1",
        "driver": "Driver 1"
    }
    response = post_request(url, data=data)
    return response.json()

def process_trip(planta, area, combination):
    trip_id = update_trip()
    try:
        logging.info(f"Processing trip for planta: {planta}, area: {area}, combination: {combination}, trip {trip_id}")
        add_trip(update_trip(), planta, *combination, area)
        logging.info(f"Successfully processed trip for planta: {planta}, area: {area}, combination: {combination}")
    except Exception as e:
        logging.error(f"Error processing trip for planta: {planta}, area: {area}, combination: {combination}. Error: {e}")

# Supuestos: listas de plantas, áreas de carga y demás parámetros ya definidas
plantas = ["PTA 1 (CD)", "Plant 4", "PTA 5 (CD)"]
area_carga = {
    "PTA 1 (CD)": ["EXPLANADA", "BODEGA"],
    "Plant 4": ["Explanada"],
    "PTA 5 (CD)": ["Explanada Arriba", "Explanada Abajo"]
}
tipo_carga = ["Carga regular", "Carga lateral"]
tipo_caja = ["Caja seca", "Plataforma"]

for planta in plantas:
    for area in area_carga[planta]:
        for combination in product(tipo_carga, tipo_caja):
            process_trip(planta, area, combination)
            time.sleep(5)

def update_sensors(plant_name, sensores_count):
    url = os.getenv("API_stagingEvent")
    sensors_status = [{"number": i + 1, "status": 0} for i in range(sensores_count)]
    return sensors_status

plant_sensor_lines = {
    "PTA 1 (CD)": 12,
    "Plant 4": 7,
    "PTA 5 (CD)": 15
}

for plant, sensors_count in plant_sensor_lines.items():
    sensors_status = update_sensors(plant, sensors_count)
    print(f"Actualización de sensores para {plant}: {sensors_status}")
