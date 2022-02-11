import requests
import json
from bs4 import BeautifulSoup
from Classes.scrapper import Scrapper

with open("choosed_items.json") as f:
    data = f.read()

file = json.loads(data)
print(file)

# response = requests.get("https://www.gamecentar.rs/playstation-4/ps4-igre.html")
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
# tags = soup.select(selector="li.item")
#
# for tag in tags:
#     titles_tag = tag.select(selector=".product_name h5")
#     prices_tag = tag.select(selector=".price-box span.price")
#     key = 0
#     for title in titles_tag:
#         current_title = title.text.strip().split(" ", 1)
#         current_price = prices_tag[key].text.strip().split(" ")[0]
#         if current_title[0].upper() == "PS4":
#             print(f"{current_title[1]}: {current_price}")

# titles_list = []
#
# for num in range(1, 29):
#     response = requests.get(f"https://www.gamecentar.rs/playstation-4/ps4-igre.html?p={num}")
#     data = response.text
#     soup = Scrapper(data)
#     soup.populate_titles_list()
#     titles_list.extend(soup.titles_list)
#
# print(titles_list)
