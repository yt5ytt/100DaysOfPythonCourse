from selenium import webdriver
import time

FIREFOX = "D:\Development\geckodriver.exe"
OOKLA_URL = "https://www.speedtest.net/"


class SpeedTest:

    download_speed = ""
    upload_speed = ""

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=FIREFOX)
        self.driver.get(OOKLA_URL)
        self.driver.maximize_window()
        time.sleep(20)
        self.press_go_button()
        time.sleep(40)
        self.down_speed()
        self.up_speed()

    def press_go_button(self):
        # press = self.driver.find_element_by_css_selector(css_selector="a span.start-text")
        press = self.driver.find_element(by="css selector", value="a span.start-text")
        press.click()

    def down_speed(self):
        self.download_speed = float(self.driver.find_element(by="class name", value="download-speed").text)

    def up_speed(self):
        self.upload_speed = float(self.driver.find_element(by="class name", value="upload-speed").text)
