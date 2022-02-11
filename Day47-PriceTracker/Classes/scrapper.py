from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self, data):
        self.titles_list = []
        self.data = data
        self.soup = BeautifulSoup(self.data, "html.parser")

    def get_tags(self):
        tags_list = self.soup.select(selector=".item .product_name h5")
        return tags_list

    def populate_titles_list(self):
        for game in self.get_tags():
            title = game.text.strip().split(" ", 1)
            if title[0].upper() == "PS4":
                self.titles_list.append(title[1])
