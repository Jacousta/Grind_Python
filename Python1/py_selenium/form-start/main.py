from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "/Users/chiragpunia/Development/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
for _ in range(10):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScuwcMpzgUygFXOAcBBp923NiQzAmGcwJYTViy9D-qVKSDTpw/viewform")

    username = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/d"
                                             "iv[1]/input")
    time.sleep(1)
    username.click()
    time.sleep(1)
    username.send_keys("chirag")
    password = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    password.click()
    time.sleep(1)
    password.send_keys("punia")
    submit = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()
    time.sleep(1)

