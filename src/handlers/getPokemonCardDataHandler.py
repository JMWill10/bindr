from dotenv import load_dotenv
import os
import requests


def getPokemonDataHandler(name: str):
    load_dotenv(".env.local")

    baseUrl = os.getenv("TCGAPI_URL")
    headers = {
        "X-API-Key": os.getenv("TCGAPI_KEY")
    }
    query_params = {
        "q": name,
        "game": "pokemon"
    }

    try:
        res = requests.get(f"{baseUrl}/search", params=query_params, headers=headers)

        res.raise_for_status()

        return res.json()
    except requests.exceptions.HTTPError as httpErr:
        return { 'error': httpErr }
    except Exception as ex:
        return { 'error': ex }