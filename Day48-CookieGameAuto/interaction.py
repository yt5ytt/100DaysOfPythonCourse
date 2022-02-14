from selenium import webdriver
from main import chrome_driver_path

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
statistics.click()

