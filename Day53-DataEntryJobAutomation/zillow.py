from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep

CHROME = "/home/yt5ytt/Development/ChromeDriver/chromedriver_linux64/chromedriver"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.6255902421875%2C%22east%22%3A-122.2410687578125%2C%22south%22%3A37.63921117178986%2C%22north%22%3A37.91112272030422%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A818937%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"


class Zillow:

    def __init__(self):
        self.driver = Chrome(executable_path=CHROME)
        self.driver.get(ZILLOW_URL)
        self.soup = BeautifulSoup(self.driver.page_source, "lxml")
        self.articles = self.soup.select("li article div.list-card-info")
        self.import_in_form()
        self.driver.quit()
    
    def import_in_form(self):
        self.google = Chrome(executable_path=CHROME)
        self.google.get("https://forms.gle/NPCpZcRjAj1QmQzVA")
        self.google.maximize_window()
        for article in self.articles:
            self.addr = article.select_one(".list-card-addr").text
            self.price = article.select_one(".list-card-price").text.split("/")[0]
            self.link = article.a["href"]
            sleep(3)
            addr = self.google.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            addr.send_keys(self.addr)
            sleep(3)
            price = self.google.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.price)
            sleep(3)
            link = self.google.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(self.link)
            sleep(3)
            button = self.google.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            button.click()
            sleep(3)
            try:
                second_answer = self.google.find_element(by="xpath", value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                second_answer.click()
                sleep(3)
            except NoSuchElementException:
                self.google.find_element(by='xpath', value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[2]/div/span/span').click()
                self.google.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span').click()
                sleep(3)



