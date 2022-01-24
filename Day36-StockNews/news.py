import requests
import os
import datetime
from alpha_vantage import AlphaVantage

API_KEY = os.environ.get("NEWS_API_KEY")
ENDPOINT = "https://newsapi.org/v2/everything"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)


class News:

    def __init__(self, r: AlphaVantage):
        self.report = r
        parametars = {
            "q": "TSLA",
            "qInTitle": "Tesla",
            "apiKey": API_KEY,
            "from": YESTERDAY,
            "to": TODAY,
            "language": "en",
        }
        self.response = requests.get(ENDPOINT, params=parametars)
        self.data = self.response.json()

    def raise_error(self):
        return self.response.raise_for_status()

    def get_title(self):
        return self.data["articles"][0]["title"]

    def get_description(self):
        return self.data["articles"][0]["description"]

    def message(self):
        return f"""
TSLA {self.report.symbol} {self.report.percentage}%
Headline: {self.get_title()}
Brief: {self.get_description()}
"""
