import os
import requests

ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
API_KEY = os.environ.get("KIWI_API_KEY")


class KiwiLocations:

    def __init__(self, city):
        headers = {
            "apikey": API_KEY,
        }
        query = {
            "term": city,
            "locale": "en_US",
            "location_types": "city",
        }
        self.response = requests.get(url=ENDPOINT, headers=headers, params=query)
        self.code = self.response.json()["locations"][0]["code"]
