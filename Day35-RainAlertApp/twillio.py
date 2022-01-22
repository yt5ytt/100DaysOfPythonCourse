from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACd75cedbaa2afafbc6a971f10a5eb0086"
TWILIO_AUTH_TOKEN = "de5cbb2f43ebccf344b26d28714128be"


class Twillio:

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
