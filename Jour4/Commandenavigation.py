import time

from selenium import webdriver
#instance de chrome
driver = webdriver.Chrome()
#maximiser
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
time.sleep(3)

driver.get("https://www.google.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)

#driver.close()