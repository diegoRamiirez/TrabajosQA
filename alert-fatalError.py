from selenium import webdriver
import time

driver = webdriver.Chrome()

file_path = "file:///Users/diegoramirez/TrabajosQA/alertSimple.html"
driver.get(file_path)
time.sleep(5)
driver.quit()
