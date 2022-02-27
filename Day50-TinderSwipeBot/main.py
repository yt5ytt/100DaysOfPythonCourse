import time
from Classes.login import Login

tinder = Login()
tinder.get_tinder()
time.sleep(5)
tinder.login_tinder()

buttons = tinder.driver.find_elements_by_tag_name("span")
for button in buttons:
    if button.text == "LOG IN WITH FACEBOOK":
        button.click()