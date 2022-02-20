import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")
CHROME = os.environ.get("CHROME")

class LinkedInLogin:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME)
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        email = self.driver.find_element_by_name("session_key")
        email.send_keys(EMAIL)
        password = self.driver.find_element_by_name("session_password")
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)

    def get_python_jobs(self):
        self.driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=1%2C2%2C3&geoId=92000000&keywords=python&location=Worldwide")

    def get_job_links(self):
        # return self.driver.find_elements_by_css_selector(css_selector="div.full-width a.job-card-list__title")
        return self.driver.find_elements_by_css_selector(css_selector="div.job-card-container--clickable")

    def save_button(self):
        save = self.driver.find_element_by_css_selector("button.jobs-save-button")
        save.click()
