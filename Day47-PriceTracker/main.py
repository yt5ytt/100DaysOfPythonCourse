import json
from Classes.sendMail import SendMail
from Classes.scrapper import Scrapper

with open("choosed_items.json") as f:
    file = f.read()

data = json.loads(file)
for item in data["choosen_products"]:
    p = Scrapper(item["link"])
    if p.get_price() != None and p.get_price() < 2000:
        mail = SendMail(item["title"], p.get_price())
