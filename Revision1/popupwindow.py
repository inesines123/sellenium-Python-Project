import time

from selenium import  webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#envoyer les identifiants par l url je mets l identifiant et mdp apres https
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(4)
driver.quit()