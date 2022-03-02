from instagram import Instagram
from time import sleep
from selenium.common.exceptions import NoSuchElementException

instagram = Instagram()
sleep(10)
instagram.login()
sleep(5)

try:
    instagram.not_now()
except NoSuchElementException:
    sleep(2)

try:
    instagram.deny_notifications()
except NoSuchElementException:
    sleep(2)

sleep(5)
instagram.search()
sleep(3)
instagram.click_followers()
sleep(3)
instagram.scroll_down()
instagram.follow()

instagram.driver.quit()
