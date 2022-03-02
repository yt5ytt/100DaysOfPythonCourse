import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

CHROME = "D:\Development\chromedriver.exe"
INSTA_URL = "https://www.instagram.com/"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class Instagram:

    num_of_followers = ""
    followers = []

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME)
        self.driver.get(INSTA_URL)
        self.driver.maximize_window()

    def login(self):
        username = self.driver.find_element(by="name", value="username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(by="name", value="password")
        password.send_keys(PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)

    def not_now(self):
        not_now = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()

    def deny_notifications(self):
        deny = self.driver.find_element(by="xpath", value='/html/body/div[6]/div/div/div/div[3]/button[2]')
        deny.click()

    def search(self):
        search = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys("openwaterswimming")
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)

    def num_followers(self, string):
        self.num_of_followers = int(string.split(" ")[0])

    def click_followers(self):
        followers = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        self.num_followers(followers.text)
        followers.click()

    def scroll_down(self):
        followers = self.driver.find_element(by="css selector", value='div._1XyCr div.isgrP')
        all_down = True
        while all_down:
            self.followers = self.driver.find_elements(by="css selector", value='div._1XyCr li')
            if self.num_of_followers - 1 > len(self.followers):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers)
                time.sleep(1)
            else:
                all_down = False

    def follow(self):
        followers = self.driver.find_elements(by="css selector", value='div._1XyCr li button')
        for follower in followers:
            if follower.text == "Follow":
                follower.click()
                time.sleep(3)

