import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#page principale
driver.get("https://opensource-demo.orangehrmlive.com/")
parentWindowId = driver.current_window_handle#CDwindow-5D7F7788A7EB4412F8AFB6D92D138783
print(parentWindowId)
#2eme fenetre
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()#CDwindow-0748664C604B06AB4B7C2481CF1B4878
#recuperer une liste d id
driver.window_handles
windowHandlesIds = driver.window_handles
parentWindowId = windowHandlesIds[0]
childWindowId = windowHandlesIds[1]
print(("parentWindowId:" ,parentWindowId))
print(("childWindowId:" ,childWindowId))
#basculer sur la deuxieme fenetre directement on swicher
driver.switch_to.window(childWindowId)
url = driver.current_url
title = driver.title
print(url)
print(title)

#lorsqu on plusiers fenetres
for windowId in windowHandlesIds:
    driver.switch_to.window(windowId)
    if driver.title == title:
        driver.close()

time.sleep(4)
driver.quit()