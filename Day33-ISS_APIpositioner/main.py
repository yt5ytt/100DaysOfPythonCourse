import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 44.270672
MY_LONG = 19.884090
API_KEY = "55edede826ce451794a3166f9b37778a"
GMAIL_SMTP = "smtp.gmail.com"
PORT = 587

USER = "alex.yt5ytt@gmail.com"
PASSWD = "Radnaskela2405976"


def send_mail():
    with smtplib.SMTP(GMAIL_SMTP, PORT) as conn:
        conn.starttls()
        conn.login(user=USER, password=PASSWD)
        conn.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg="Subject: ISS is close\nGet outside and look up in the sky!"
        )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print("60s")

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 < iss_lat < MY_LAT + 5) and (MY_LONG - 5 < iss_long < MY_LONG + 5):
        return True


def is_night():
    response = requests.get(f"https://api.ipgeolocation.io/astronomy?apiKey={API_KEY}&lat={MY_LAT}&long={MY_LONG}")
    response.raise_for_status()
    datas = response.json()
    my_sunrise_hour = int(datas["sunrise"].split(":")[0])
    my_sunset_hour = int(datas["sunset"].split(":")[0])

    time_now = int(datetime.now().hour)

    if time_now > my_sunset_hour or time_now < my_sunrise_hour:
        return True


while True:
    if is_night() and is_iss_overhead():
        send_mail()
    time.sleep(60)


