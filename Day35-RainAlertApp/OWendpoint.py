import requests
import os

LAT = 44.270672
LONG = 19.884090
API_KEY = os.environ.get("OWM_API_KEY")

class OW_endpoint:

    def __init__(self):
        self.ow_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
        self.parameters = {
            "lat": LAT,
            "lon": LONG,
            "exclude": "current,minutely,daily,alerts",
            "units": "metric",
            "appid": API_KEY,
        }
        self.response = requests.get(self.ow_endpoint, params=self.parameters)

    def json(self):
        return self.response.json()

    def raise_error(self):
        return self.response.raise_for_status()
