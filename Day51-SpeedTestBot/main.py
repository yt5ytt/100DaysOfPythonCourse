import time
from Classes.ookla import SpeedTest
from Classes.twitter import Twitter

ookla = SpeedTest()

twitter = Twitter(ookla)
if twitter.is_slower():
    twitter.complaine_tweat()

ookla.driver.quit()
twitter.driver.quit()

