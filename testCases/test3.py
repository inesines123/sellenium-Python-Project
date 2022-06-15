#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
import time

from selenium.webdriver.chrome.service import  Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# service_obj = Service("C:\\Users\\Ines\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/# 3)
from testCases.test2 import driver

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
# ouvrir la page
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
act_title =  driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
time.sleep(10)
driver.close()
