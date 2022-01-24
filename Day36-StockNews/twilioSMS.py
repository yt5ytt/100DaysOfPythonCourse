from twilio.rest import Client
import os
from news import News
from alpha_vantage import AlphaVantage

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.environ.get("TO_NUMBER")
FROM_NUMBER = os.environ.get("FROM_NUMBER")


class TwilioSMS:

    def __init__(self, n: News, r: AlphaVantage):
        self.news = n
        self.report = r
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def message(self, title, description):
        return f"""
TSLA {self.report.symbol} {self.report.percentage}%
Headline: {title}
Brief: {description}
"""

    def sms(self):
        for article in self.news.three_articles:
            message = self.client.messages \
                .create(
                    body=f"{self.message(article['title'], article['description'])}",
                    from_=FROM_NUMBER,
                    to=TO_NUMBER
                )
            print(message.status)
