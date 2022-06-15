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

#mettre du temps d arret
time.sleep(4)
#fermeture du navigateu
driver.close()