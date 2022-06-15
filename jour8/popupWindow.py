import time

from gererframe import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(4)
driver.quit()