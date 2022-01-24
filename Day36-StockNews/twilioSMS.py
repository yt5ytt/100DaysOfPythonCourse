from twilio.rest import Client
import os
from news import News

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.environ.get("TO_NUMBER")
FROM_NUMBER = os.environ.get("FROM_NUMBER")


class TwilioSMS:

    def __init__(self, n: News):
        self.news = n
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def sms(self):
        message = self.client.messages \
            .create(
                body=f"{self.news.message()}",
                from_=FROM_NUMBER,
                to=TO_NUMBER
            )
        print(message.status)
