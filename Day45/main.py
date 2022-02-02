from bs4 import BeautifulSoup
import requests

MY_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(MY_URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.select(selector=".listicle-item img")

movies_list = [title.get("alt") for title in titles if title.get("alt") != "Amazon"]
index = len(movies_list)

number = 0
while index > 0:
    number += 1
    with open("movies_list.txt", "a") as f:
        f.write(f"{number}) {movies_list[index-1]}\n")
    print(f"{number}) {movies_list[index-1]}")
    index -= 1
