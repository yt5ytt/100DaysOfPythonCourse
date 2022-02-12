import smtplib
import os

GMAIL_SMTP = "smtp.gmail.com"
PORT = 587

USER = os.environ.get("USER")
PASSWD = os.environ.get("PASSWD")

class SendMail:

    def __init__(self, title, price):
        with smtplib.SMTP(GMAIL_SMTP, PORT) as self.conn:
            self.conn.starttls()
            self.conn.login(user=USER, password=PASSWD)
            self.conn.sendmail(
            from_addr=USER,
            to_addrs="yt5ytt@gmail.com",
            msg=f"Subject: Nove cene na odabrane igrice u GameCentru\nPozuri da kupis igricu po super ceni\n\n{title}\n\nza samo {price},00 dinara\n\nTvoj GameCentar PYTHON podsetnik!!!"
        )