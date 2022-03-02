import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Classes.ookla import SpeedTest

CHROME = "D:\Development\chromedriver.exe"
USERNAME = os.environ.get("USERNAME")
TWITTER_URL = os.environ.get("TW_URL")
TWITTER_USER = os.environ.get("USER")
TWITTER_PASS = os.environ.get("PASS")


class Twitter:

    def __init__(self, ookla: SpeedTest):
        self.ookla = ookla
        self.driver = webdriver.Chrome(CHROME)
        self.driver.get(TWITTER_URL)
        self.driver.maximize_window()
        time.sleep(5)
        self.insert_email()
        time.sleep(5)
        self.insert_password()

    def insert_email(self):
        email = self.driver.find_element(by="name", value="text")
        email.send_keys(TWITTER_USER)
        time.sleep(3)
        email.send_keys(Keys.ENTER)

    def insert_password(self):
        try:
            password = self.driver.find_element(by="name", value="password")
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(by="name", value="text")
            username.send_keys(USERNAME)
            time.sleep(3)
            username.send_keys(Keys.ENTER)
            time.sleep(10)
            password = self.driver.find_element(by="name", value="password")
            password.send_keys(TWITTER_PASS)
            time.sleep(3)
            password.send_keys(Keys.ENTER)
            time.sleep(10)

    def is_slower(self):
        if self.ookla.download_speed < 250 or self.ookla.upload_speed < 25:
            return True
        else:
            return False

    def complaine_tweat(self):
        text = f"Dragi moj provajderu! Zasto je brzina {self.ookla.download_speed}/{self.ookla.upload_speed}Mbps " \
               f"kada placam brzinu po ugovoru 250/25Mbps?"
        tweet = self.driver.find_element(by="css selector", value=".notranslate")
        tweet.send_keys(text)
        tweet_button = self.driver.find_element(by="css selector", value="div.r-l5o3uw:nth-child(4)")
        tweet_button.click()
