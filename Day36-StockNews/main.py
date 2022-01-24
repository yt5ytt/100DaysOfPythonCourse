from alpha_vantage import AlphaVantage
from news import News
from twilioSMS import TwilioSMS

r = AlphaVantage()
r.raise_error()

n = News()
n.raise_error()

t = TwilioSMS(n, r)
if r.is_fluctuation():
    t.sms()
