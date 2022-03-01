import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Classes.ookla import SpeedTest
from const import FIREFOX, TWITTER_URL, TWITTER_USER, TWITTER_PASS

USERNAME = os.environ.get("USERNAME")


class Twitter:

    def __init__(self, ookla: SpeedTest):
        self.ookla = ookla
        self.driver = webdriver.Firefox(executable_path=FIREFOX)
        self.driver.get(TWITTER_URL)
        self.driver.maximize_window()
        time.sleep(5)
        self.insert_email()
        time.sleep(5)
        self.insert_password()

    def insert_email(self):
        email = self.driver.find_element_by_name("text")
        email.send_keys(TWITTER_USER)
        email.send_keys(Keys.ENTER)

    def insert_password(self):
        try:
            password = self.driver.find_element_by_name("password")
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element_by_name("text")
            username.send_keys(USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(20)
        else:
            # self.driver.switch_to.frame(self.other_frame())
            password = self.driver.find_element_by_css_selector(css_selector=".r-1867qdf .r-homxoj")
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
            time.sleep(10)

    # def other_frame(self):
    #     return self.driver.find_element_by_css_selector(css_selector=".r-1867qdf")

    def is_slower(self):
        if self.ookla.download_speed < 250 or self.ookla.upload_speed < 25:
            return True
        else:
            return False

    def complaine_tweat(self):
        text = f"Dragi moj provajderu! Zasto je brzina {self.ookla.download_speed}/{self.ookla.upload_speed} kada placam brzinu po ugovoru 250/25?"
        tweat = self.driver.find_element_by_css_selector(css_selector=".notranslate")
        tweat.send_keys(text)
        tvituj = self.driver.find_element_by_css_selector(css_selector="div.r-l5o3uw:nth-child(4)")
        tvituj.click()
