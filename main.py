from fastapi import FastAPI
from fastapi.responses import FileResponse
from logic.equake_logic import EquakeLogic

app = FastAPI()
logic = EquakeLogic()

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.get("/earthquakes")
def get_earthquakes(timeframe: str, group: str):
    return logic.request_data(timeframe, group)