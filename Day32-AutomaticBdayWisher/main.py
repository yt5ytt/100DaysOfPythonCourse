import datetime as dt
import pandas
import random
import smtplib

SMTP_PORT = 587

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_USER = "alex.yt5ytt@gmail.com"
GMAIL_PASS = "Radnaskela2405976"

now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("bday_list.csv")
rows = data.iterrows()

for index, row in rows:
    if row.month == month and row.day == day:
        letter_num = random.randint(1, 3)

        with open(f"./letters_templates/letter_{letter_num}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", row.ime)

        with smtplib.SMTP(GMAIL_SMTP, SMTP_PORT) as conn:
            conn.starttls()
            conn.login(user=GMAIL_USER, password=GMAIL_PASS)
            conn.sendmail(
                from_addr=GMAIL_USER,
                to_addrs=row.email,
                msg=f"Subject: Srecan rodjendan {row.ime}\n{letter}"
            )
