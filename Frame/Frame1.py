import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
#swicher vers le frame:
driver.switch_to.frame("packageListFrame")
time.sleep(3)
#pour sortir de ce frame
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")


time.sleep(4)
driver.quit()