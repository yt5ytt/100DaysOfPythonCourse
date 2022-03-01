import time
from Classes.tinder import Login

tinder = Login()
tinder.get_tinder()
time.sleep(5)
tinder.login_tinder()
time.sleep(10)

tinder.like()

tinder.driver.quit()
