import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#cliquer sur boutton
driver.find_element(By.XPATH, "//button[contains(text(),'Alert')]").click()

#creer une altert que ja appelle alertwindow et je bascule sur alertje suis a interieur
alertWindow = driver.switch_to.alert
#recupere le texte ds l alert
print(alertWindow.text)
#cliquer sur le bouton ok de l alert
alertWindow.accept()

time.sleep(5)
driver.quit()#ferme tte la fenetre 