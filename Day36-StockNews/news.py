import requests
import os
import datetime

API_KEY = os.environ.get("NEWS_API_KEY")
ENDPOINT = "https://newsapi.org/v2/everything"
TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)


class News:

    def __init__(self):
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
        self.three_articles = self.get_three_articles()

    def raise_error(self):
        return self.response.raise_for_status()

    def get_three_articles(self):
        return self.data["articles"][:3]
