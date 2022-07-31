from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "/Users/chiragpunia/Development/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, "//*[@id='cookie']")


time.sleep(5)

for x in range(1000):
    cookie.click()
