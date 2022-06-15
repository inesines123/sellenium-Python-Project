from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#cliquer sur boutton
driver.find_element(By.XPATH, "//button[contains(text(),'Prompt')]").click()
time.sleep(5)
driver.switch_to.alert.send_keys("Bonjour")

driver.switch_to.alert.accept()


time.sleep(2)
driver.close()

