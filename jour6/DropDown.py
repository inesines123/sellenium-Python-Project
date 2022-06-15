import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
#selection = driver.find_element_by_name("q")

#selection.send_keys("Country")
#driver.findElement(By.name("q")).sendKeys("Tunisia");

#input-country
dropCountry = driver.find_element(By.ID, "input-country")
country = Select(dropCountry)
country.select_by_visible_text("Tunisia")
country.select_by_index(0)
country.select_by_value("167")
#recuperer toutes les selections dans select
allOptions = country.options
totalOptions = len(allOptions)
# print("le nombre total d options :", totalOptions)
# for opt in allOptions:
#     print(opt.text)
#selection une option particuliere
for opt in allOptions:

    if opt.text == "Canada":
        opt.click()
        break
s
