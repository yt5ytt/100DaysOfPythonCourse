import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"


class Billboard:
    title_list = []

    def __init__(self, date):
        response = requests.get(f"{BILLBOARD_URL}/{date}/")
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        titles = soup.select(selector="ul li h3.c-title")
        title_list = [title.getText() for title in titles]

        for title in title_list:
            self.title_list.append(title.strip())