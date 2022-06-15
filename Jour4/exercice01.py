# test case
# 1 lancer navigateur
# 2 acceder a l adresse "https://www.saucedemo.com/"
# 3 saisir username
# 4 saisir password
# 5 cliquer sur login
# 6 cliquer sur add to cart
# 7 cliquer sur panier
# 8 cliquer sur ckekout
# 9 saisir firstname
# 10 saisir last name
# 11 saisir code postal
# 12 cliquer sur cancel

import time

from selenium import webdriver
#instance vide de chrome
from selenium.webdriver.common.by import By

# 1 lancer le navigateur
driver = webdriver.Chrome()
#ouvrir la fenetre en plein ecran
driver.maximize_window()
# 2 acceder a l "adresse https://www.saucedemo.com/"
driver.get("https://www.saucedemo.com/")
# 3 saisir username
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# 4 saisir password
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
# 5 cliquer sur login
driver.find_element(By.NAME, "login-button").submit()
# 6 cliquer sur add to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
# 7 cliquer sur panier
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# 8 cliquer sur ckekout
driver.find_element(By.NAME, "checkout").click()
# 9 saisir firstname
driver.find_element(By.ID, "first-name").send_keys("Ines")
# 10 saisir last name
driver.find_element(By.ID, "last-name").send_keys("ksibi")
# 11 saisir code postal
driver.find_element(By.NAME, "postalCode").send_keys("J4W2W5")
# 12 cliquer sur cancel
driver.find_element(By.NAME, "cancel").click()

#mettre du temps d arret
time.sleep(4)
#fermeture du navigateu
driver.close()

