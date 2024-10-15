from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

file_path = "file:///Users/diegoramirez/TrabajosQA/alertSimple.html"
driver.get(file_path)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "alert")))
alert_simple = driver.find_element(By.NAME, "alert")
alert_simple.click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
driver.quit()
