import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuración de la API
API_BASE_URL = "https://zara-boost-hackathon.nuwe.io/users/"
MAX_WORKERS = 20  # Número de hilos
SAVE_INTERVAL = 500  # Guardar progreso cada X usuarios
OUTPUT_FILE = "user_details.json"
USER_IDS_FILE = "/home/pablost/Hackathon_inditex_data_science/hackathon-inditex-data-recommender/notebooks/user_ids.json"


# Función para consultar los detalles de un usuario
def fetch_user_details(user_id, retries=5, delay=2):
    """
    Consulta los detalles de un usuario con reintentos en caso de error.
    """
    url = f"{API_BASE_URL}{user_id}"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Genera excepción si hay problemas HTTP
            data = response.json()
            logging.info(f"Fetched data for user_id {user_id}")
            return {
                "user_id": data["user_id"],
                "country": data["values"].get("country", []),
                "R": data["values"].get("R", []),
                "F": data["values"].get("F", []),
                "M": data["values"].get("M", [])
            }
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt + 1} failed for user_id {user_id}: {e}")
            time.sleep(delay)
    logging.error(f"Max retries exceeded for user_id {user_id}")
    return None

# Función para consultar todos los usuarios
def fetch_all_users(user_ids):
    """
    Consulta los detalles de todos los usuarios utilizando paralelismo.
    """
    user_records = []
    failed_user_ids = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_user = {executor.submit(fetch_user_details, user_id): user_id for user_id in user_ids}

        for i, future in enumerate(as_completed(future_to_user)):
            user_id = future_to_user[future]
            try:
                result = future.result()
                if result:
                    user_records.append(result)
                else:
                    failed_user_ids.append(user_id)
            except Exception as exc:
                logging.error(f"User {user_id} generated an exception: {exc}")
                failed_user_ids.append(user_id)

            # Guardar progreso incremental
            if (i + 1) % SAVE_INTERVAL == 0:
                save_to_json(user_records, OUTPUT_FILE)
                logging.info(f"Progress saved after {i + 1} users")

    # Reintentos para usuarios fallidos
    while failed_user_ids:
        logging.info(f"Retrying for {len(failed_user_ids)} failed user IDs...")
        remaining_failed_ids = []

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_user = {executor.submit(fetch_user_details, user_id): user_id for user_id in failed_user_ids}

            for future in as_completed(future_to_user):
                user_id = future_to_user[future]
                try:
                    result = future.result()
                    if result:
                        user_records.append(result)
                    else:
                        remaining_failed_ids.append(user_id)
                except Exception as exc:
                    logging.error(f"User {user_id} generated an exception: {exc}")
                    remaining_failed_ids.append(user_id)

        failed_user_ids = remaining_failed_ids

    save_to_json(user_records, OUTPUT_FILE)
    return user_records

# Función para guardar datos en un archivo JSON
def save_to_json(data, filename):
    """
    Guarda los datos en un archivo JSON.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"Data saved to {filename}")

# Ejecución principal
if __name__ == "__main__":
    # Cargar los IDs de los usuarios desde el archivo
    with open(USER_IDS_FILE, "r") as f:
        user_ids = json.load(f)

    logging.info(f"Total user IDs to query: {len(user_ids)}")

    # Consultar todos los usuarios
    fetch_all_users(user_ids)
