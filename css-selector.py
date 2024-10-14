from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)
content = driver.find_element(By.CSS_SELECTOR, 'a.w3-blue')
content.click()

driver.quit()