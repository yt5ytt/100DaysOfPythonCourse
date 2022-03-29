from smtplib import SMTP
import os

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_USER = os.environ.get("USERNAME")
GMAIL_PASS = os.environ.get("PASSWORD")
SMTP_PORT = 587


class SendMail:

    def __init__(self, email, name, message):
        with SMTP(GMAIL_SMTP, SMTP_PORT) as conn:
            conn.starttls()
            conn.login(user=GMAIL_USER, password=GMAIL_PASS)
            conn.sendmail(
                from_addr=email,
                to_addrs=GMAIL_USER,
                msg=f"Subject: {name} sa mail adresom {email} Vam je poslao poruku sa sajta\n{message}"
        )