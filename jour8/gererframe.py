import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Entrer dans le frame
driver.switch_to.frame("packageListFrame")
time.sleep(3)

# Cliquez sur le lien
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

time.sleep(3)
driver.quit()


