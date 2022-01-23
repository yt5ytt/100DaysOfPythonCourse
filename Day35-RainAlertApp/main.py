from OWendpoint import OW_endpoint
from twilioSMS import TwilioSMS

response = OW_endpoint()
response.raise_error()
data = response.json()

will_rain = False
for num in range(12):
    hour_data = data["hourly"][num]
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    send = TwilioSMS()
    send.sms()
else:
    print("You don't need an umbrella in the next 12 hours.")
