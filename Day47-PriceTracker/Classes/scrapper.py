import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self, link):
        self.link = link
        response = requests.get(link)
        data = response.text
        self.soup = BeautifulSoup(data, "html.parser")
    
    def get_price(self):
        price_tag = self.soup.select(selector="div.price-info strike span.price")
        if len(price_tag) != 0:
            discount_tag = self.soup.select(selector="div.price-info p.special-price span.price")
            for price_tag in discount_tag:
                price = self.get_price_int(price_tag.getText().strip())
                return price
    
    def get_price_int(self,raw_price):
        price_list = raw_price.split(".")
        lower_price = price_list[1].split(",")[0]
        price = f"{price_list[0]}{lower_price}"
        return int(price)