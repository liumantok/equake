from datetime import datetime, timezone
import requests

class equakeLogic():

    def __init__(self):
        pass
    
    def analyzeInput(self, input): #doesnt do shit for now
        return input == "wo shi"
    
    def requestData(self): #horrible i know. will do for now
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
        response = requests.get(url)
        data = response.json()

        #print(f"Number of earthquakes in the last month: {len(data['features'])}")

        def convertTime(time):
            utc_time = datetime.fromtimestamp(time / 1000, tz=timezone.utc)
            return utc_time

        for eq in data['features'][:1]:
            place = eq['properties']['place']
            mag = eq['properties']['mag']
            time = convertTime(eq['properties']['time'])
            msg = (f"Magnitude {mag} - {place} - {time}")
            return msg