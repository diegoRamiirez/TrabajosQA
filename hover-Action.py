
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(3)
elem = driver.find_element_by_link_text("Privacidad")

hover = ActionChains(driver).move_to_element(elem)
hover.perform()
driver.quit()