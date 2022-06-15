#test case
# 1 lancer le navigateur
# 2 lancer le navigateur www.google.ca
# 3 saisir selenium sur le champs de de recherche
# 4 cliquer sur seleniumwebdriver

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 2 lancer le navigateur www.google.ca
driver.get("https://www.google.ca/")

# 3 saisir selenium sur le champs de de recherche
selection = driver.find_element_by_name("q")

selection.send_keys("selenium")
# element.select_by_value("def")
#
# #recuperer ttes les options ds select
# allOptions = element.options
# #pour savoir la taille des elements
# totalOptions = len(allOptions)
# print("Le nombre total d options :", totalOptions)
# #je veux afficher tt les options ds la console
# # for opt in allOptions:
# #     print(opt.text)
#
# #je veux selectionner une option particuliére
# for opt in allOptions:
#     if opt.text == "doc 2":
#         opt.click()
# #pour optimiser mon script
#         break