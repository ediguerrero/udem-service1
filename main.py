from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/infoUsers/{idUsuario}")
def read_item(idUsuario: str):
    url = 'https://62fc4666abd610251c17fdae.mockapi.io/api/User/?idUsuario=' + idUsuario
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json()}
