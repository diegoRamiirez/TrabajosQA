from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)

all_cookies = driver.get_cookies()

print(all_cookies)
