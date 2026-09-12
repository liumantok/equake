from datetime import datetime, timezone
import requests

class equakeLogic():

    def __init__(self):
        self.parameters = {
        "Past hour" : "hour",
        "Past day" : "day",
        "Past 7 days" : "week",
        "Past 30 days" : "month",

        "Significant" : "significant",
        "M4.5+" : "4.5",
        "M2.5+" : "2.5",
        "M1.0+" : "1.0",
        "All" : "all"
    }
    def convertTime(self, time):
        utc_time = datetime.fromtimestamp(time / 1000, tz=timezone.utc)
        return utc_time
    
    def requestData(self, timeframe, group):
        timeframe = self.parameters[timeframe]
        group = self.parameters[group]

        url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{group}_{timeframe}.geojson"

        response = requests.get(url)
        data = response.json()
        msg = ""
        for eq in data['features'][:5]:
            place = eq['properties']['place']
            mag = eq['properties']['mag']
            time = self.convertTime((eq['properties']['time']))
            msg = msg + (f"Magnitude {mag} - {place} - {time}")
        return msg