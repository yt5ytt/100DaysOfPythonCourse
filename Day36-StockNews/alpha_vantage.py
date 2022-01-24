import os
import requests
import itertools

API_KEY = os.environ.get("AV_API_KEY")
ENDPOINT = "https://www.alphavantage.co/query"


class AlphaVantage:

    def __init__(self):
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "TSLA",
            "datatype": "json",
            "apikey": API_KEY,
        }
        self.response = requests.get(ENDPOINT, params=parameters)
        self.daily = self.response.json()["Time Series (Daily)"]
        pair = dict(itertools.islice(self.daily.items(), 2))
        self.data = [value for key, value in pair.items()]
        self.today = float(self.data[0]["4. close"])
        self.yesday = float(self.data[1]["4. close"])
        self.percentage = self.percentage()
        self.symbol = self.symbol()

    def raise_error(self):
        return self.response.raise_for_status()

    def percentage(self):
        if self.today > self.yesday:
            diff = self.today - self.yesday
        else:
            diff = self.yesday - self.today
        percentage = round(diff/self.yesday * 100, 2)
        return percentage

    def is_fluctuation(self):
        if self.percentage > 10:
            return True
        else:
            return False

    def symbol(self):
        if self.today > self.yesday:
            symbol = "⬆"
        else:
            symbol = "⬇"
        return symbol
