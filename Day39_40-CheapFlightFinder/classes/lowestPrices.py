import os
import requests

SHEETY_END = os.environ.get("SHEETY_END")


class LowestPrices:

    def __init__(self):
        self.response = requests.get(SHEETY_END)
        self.data = self.response.json()["prices"]

    def import_codes(self, row_id, code):
        body = {
            "prices": {
                "id": row_id,
                "iataCode": code,
            }
        }
        self.response = requests.put(url=f"{SHEETY_END}/{id}", json=body)
