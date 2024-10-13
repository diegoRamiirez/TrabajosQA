from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)

try:
    displayelementRechazar = driver.find_element(By.NAME, "Rechazar todo")
    displayelementRechazar.click()
except:
    print("No se encontró el botón de Rechazar todo")
    
time.sleep(3)

try:
    displayelement = driver.find_element(By.NAME, "btnI")
    print(displayelement.is_enabled())  # Comprueba si el botón está habilitado
    print(displayelement.is_displayed())  # Comprueba si el botón está visible
except:
    print("No se encontró el botón 'Voy a tener suerte'")

driver.quit()