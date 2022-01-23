from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


class TwilioSMS:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def sms(self):
        message = self.client.messages \
            .create(
                body="It will going to rain, bring an ☂",
                from_="+16075245907",
                to="+381605991001"
            )
        print(message.status)
