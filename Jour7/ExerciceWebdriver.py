import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
#je recupere l element de select
dropElement = driver.find_element(By.ID, "drop1")
element = Select(dropElement)
#il va me selectionner une valeur par texte visible
# element.select_by_visible_text("doc 1")
# element.select_by_visible_text("doc 2")
# element.select_by_visible_text("doc 3")
# element.select_by_visible_text("doc 4")

#l ordre de selection
#element.select_by_index(0)

#autre methode de selection
element.select_by_value("def")

#recuperer ttes les options ds select
allOptions = element.options
#pour savoir la taille des elements
totalOptions = len(allOptions)
print("Le nombre total d options :", totalOptions)
#je veux afficher tt les options ds la console
# for opt in allOptions:
#     print(opt.text)

#je veux selectionner une option particuliére
for opt in allOptions:
    if opt.text == "doc 2":
        opt.click()
#pour optimiser mon script
        break

time.sleep(3)
driver.close()



