import requests
from selenium import webdriver
from bs4 import BeautifulSoup

FIREFOX = "D:\Development\geckodriver.exe"
ZILLOW_URL = "https://www.google.com/"


class Zillow:

    html_code = ""

    def __init__(self):
        self.html()
        self.soup = BeautifulSoup(self.html_code, "html.parser")
        print(self.soup.prettify())

    def html(self):
        self.html_code = requests.get(ZILLOW_URL).text


