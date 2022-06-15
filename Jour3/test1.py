# test case
# 1 lancer le navigateur
# 2 acceder a l "adresse https://demo.nopcommerce.com/"
# 3 cliquer sur le lien register
# 4 remplir le formulaire
# 5 cliquer sur le bouton register
import time

from selenium import webdriver
#instance vide de chrome
from selenium.webdriver.common.by import By

# 1 lancer le navigateur
driver = webdriver.Chrome()
#ouvrir la fenetre en plein ecran
driver.maximize_window()
# 2 acceder a l "adresse https://demo.nopcommerce.com/"
driver.get("https://demo.nopcommerce.com/")
# 3 cliquer sur le lien register j utilise le localistaeur link test
# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()#recherche par nom partiel du lien
# 4 remplir le formulaire
driver.find_element(By.ID, "FirstName").send_keys("Ines")
driver.find_element(By.NAME, "LastName").send_keys("KSIBI")
driver.find_element(By.ID, "Email").send_keys("inesksibi@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
driver.find_element(By.ID, "register-button").submit()
driver.find_element(By.CLASS_NAME, "ico-login").submit()
#mettre du temps d arret
time.sleep(4)
#fermeture du navigateu
driver.close()