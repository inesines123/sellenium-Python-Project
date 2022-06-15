#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#la classe service va nous aider pour trouver le chemin vers notre driver
#je cree un objet chrome je vais tester l application sur google chrome tt en specifiant le chemin de chrome
from selenium.webdriver.common.by import By

#service_obj = Service("C:\\Users\\Ines\\Desktop\chromedriver_win32\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
#driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://login.salesforce.com/?locale=fr-ca
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/?locale=fr-ca")
driver.maximize_window()#pour maximiser
#3) Entrer username (Ines)
driver.find_element(By.ID, "username").send_keys("Ines")
# 4) Entrer password ()
driver.find_element(By.ID, "password").send_keys("ines")
# 5) Cliquer sur le bouton tologin
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title
# 7) Verifier le titre de la page: Salesforce  (attendu)
exp_title = "Connexion | Salesforce"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
time.sleep(200)
# 8) Fermer le navigateur
driver.close()