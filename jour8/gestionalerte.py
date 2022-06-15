import time

import click
from gererframe import webdriver
from gererframe.webdriver.common.alert import Alert
from gererframe.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#affichage de message d alert
driver.find_element(By.XPATH, "//button[contains(text(),'Alert')]").click()
#recuperer le texte de l alerte
alertWindow = driver.switch_to.alert
textAlert = alertWindow.text
#pour l afficher
print("le texte de l alerte est :" ,textAlert)
#cliquer sur le boutton de l alerte
alertWindow.accept()

time.sleep(5)
driver.quit()#fermer ttes les fenetres qui sont ouverte par le script