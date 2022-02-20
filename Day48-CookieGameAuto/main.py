from selenium import webdriver
import time

chrome_driver_path = 'D:\Development\geckodriver.exe'

driver = webdriver.Firefox(chrome_driver_path)
driver.get("http://orteil.dashnet.org/cookieclicker/")

#Get cookie to click on.
cookie = driver.find_element_by_id("bigCookie")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    # if time.time() > timeout:

    #     products = driver.find_elements_by_css_selector("#products div.enabled")
    #     if len(products) > 0:
    #         products[len(products) - 1].click()
        
    #     upgrades = driver.find_elements_by_css_selector("#upgrades div.enabled")
    #     if len(upgrades) > 0:
    #         upgrades[len(upgrades) - 1].click()
        
    #     #Add another 5 seconds until the next check
    #     timeout = time.time() + 5