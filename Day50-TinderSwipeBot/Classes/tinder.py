import os
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME = "D:\Development\chromedriver.exe"
TINDER = "https://tinder.com/"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASS")


class Login:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME)
    
    def get_tinder(self):
        return self.driver.get(TINDER)
    
    def login_tinder(self):
        self.driver.maximize_window()
        cookies_button = self.driver.find_element_by_xpath('//*[@id="s1502865376"]/div/div[2]/div/div/div[1]/button')
        cookies_button.click()
        login = self.driver.find_element_by_xpath('//*[@id="s1502865376"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login.click()
        time.sleep(5)
        facebook = self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        facebook.click()
        time.sleep(5)
        self.driver.switch_to.window(self.fb_window())
        time.sleep(5)
        self.login_fb()
        time.sleep(2)
        self.driver.switch_to.window(self.base_window())
        time.sleep(20)
        self.popup_cancelation()

    def login_fb(self):
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(EMAIL)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def base_window(self):
        return self.driver.window_handles[0]

    def fb_window(self):
        return self.driver.window_handles[1]

    def popup_cancelation(self):
        popup1 = self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div/div/div[3]/button[1]')
        popup1.click()
        time.sleep(2)
        popup2 = self.driver.find_element_by_xpath('//*[@id="s-225515700"]/div/div/div/div/div[3]/button[1]')
        popup2.click()

    def like(self):
        for n in range(100):
            time.sleep(5)
            try:
                like = self.driver.find_element_by_xpath('//*[@id="s1502865376"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                like.click()
            except NoSuchElementException:
                self.driver.refresh()
            except ElementClickInterceptedException:
                self.driver.refresh()

