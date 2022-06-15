import time

from selenium import webdriver
#instance de chrome
driver = webdriver.Chrome()
#maximiser
driver.maximize_window()
#obtenir l url de la page
driver.get("https://demo.nopcommerce.com/")
url_page = driver.current_url
print(url_page)

#obtenir title
titre_page = driver.title
print(titre_page)

#obtenir code source
source_page = driver.page_source
print(source_page)



time.sleep(3)
driver.close()