import os
import requests
import datetime

KIWI_END = "https://tequila-api.kiwi.com/v2/search"
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_ID = os.environ.get("KIWI_ID")


class KiwiFlights:

    def __init__(self, iata):
        self.today = datetime.date.today()
        parameters = {
            "fly_from": "BEG",
            "fly_to": iata,
            "dateFrom": self.get_date_from(),
            "dateTo": self.get_date_to(),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
        }
        headers = {
            "apikey": KIWI_API_KEY,
        }
        self.response = requests.get(url=KIWI_END, params=parameters, headers=headers)
        self.data = self.response.json()["data"]

    def get_date_from(self):
        date = self.today + datetime.timedelta(days=1)
        return date.strftime("%d/%m/%Y")

    def get_date_to(self):
        date = self.today + datetime.timedelta(days=180)
        return date.strftime("%d/%m/%Y")
