import requests

LAT = 44.270672
LONG = 19.884090
# LAT = 52.520008
# LONG = 13.404954
API_KEY = "cb2d76f21d73982f7deb1422cf938db4"


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
