from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from logic.equake_logic import EquakeLogic

app = FastAPI()
logic = EquakeLogic()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.get("/earthquakes")
def get_earthquakes(timeframe: str, group: str):
    return logic.request_data(timeframe, group)