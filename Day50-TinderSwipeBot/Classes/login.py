import os
from selenium import webdriver

CHROME = "/home/yt5ytt/Development/ChromeDriver/chromedriver_linux64/chromedriver"
TINDER = "https://tinder.com/"

class Login:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME)
    
    def get_tinder(self):
        return self.driver.get(TINDER)
    
    def login_tinder(self):
        login = self.driver.find_element_by_link_text("Log in")
        login.click()