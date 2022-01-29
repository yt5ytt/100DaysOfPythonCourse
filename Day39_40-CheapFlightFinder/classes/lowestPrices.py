import os
import requests

SHEETY_END = os.environ.get("SHEETY_END")


class LowestPrices:

    def __init__(self):
        self.response = requests.get(SHEETY_END)
        self.data = self.response.json()["list1"]
