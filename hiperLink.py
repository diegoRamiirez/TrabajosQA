from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.w3schools.com/")
time.sleep(5)

encontrar_link = driver.find_element(By.LINK_TEXT, 'Learn PHP')
encontrar_link.click()

driver.quit()