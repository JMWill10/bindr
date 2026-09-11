import requests
import os
from dotenv import load_dotenv

load_dotenv(".env.local")

baseUrl = "https://api.tcgapi.dev/v1"

query_params = {
    "q": "mew",
    "game": "pokemon"
}

headers = {
    "X-API-Key": os.getenv("TCGAPI_KEY")
}

try:
    response = requests.get(f"{baseUrl}/search", params=query_params, headers=headers)

    response.raise_for_status()

    card_data = response.json()
    print("Got Card Data:")
    print(card_data)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")