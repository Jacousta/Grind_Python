from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.linkedin.com/jobs/search/?currentJ" \
      "obId=3179313645&f_AL=true&keywords=python%20developer"
email = "chiragpunia750@yahoo.com"
password = "mitul0011"
mobile_no = "9501545441"
signin_path = "/html/body/div[1]/header/nav/div/a[2]"
email_path = "//*[@id='username']"
password_path = "//*[@id='password']"
sign_in_complete_path = "//*[@id='organic-div']/form/div[3]/button"
code_path = "//*[@id='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalize" \
            "d_jobPosting:3190950855,63889827,phoneNumber~country)']"
india_path = "//*[@id='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3190950855,63889827,phoneNumber~country)']/option[104]"
apply_path = "//*[@id='ember360']"
option_path = "//*[@id='urn:li:fs_easyApplyFormElement:" \
              "(urn:li:fs_normalized_jobPosting:3190950855,63889827,phoneNumber~nationalNumber)']"
next_path = "//*[@id='ember376']/span"
review_path = "//*[@id='ember382']/span"
submit_path = "//*[@id='ember392']/span"
driver_path = "/Users/chiragpunia/Development/chromedriver"
q1_path = "//*[@id='urn:li:fs_easyApplyFormElement:(ur" \
          "n:li:fs_normalized_jobPosting:3190950855,63890019,numeric)']"
q2_path = "//*[@id='urn:li:fs_easyApplyFormElement:(ur" \
          "n:li:fs_normalized_jobPosting:3190950855,63890003,numeric)']"
q3_path = "//*[@id='urn:li:fs_easyApplyFormEleme" \
          "nt:(urn:li:fs_normalized_jobPosting:3190950855,63890011,numeric)']"
a1 = "1"
a2 = "0"
a3 = "0"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

signin = driver.find_element(By.XPATH, signin_path)
signin.click()

mail = driver.find_element(By.XPATH, email_path)
mail.click()
mail.send_keys(email)

time.sleep(1)

password_1 = driver.find_element(By.XPATH, password_path)
password_1.click()
password_1.send_keys(password)

time.sleep(1)

complete = driver.find_element(By.XPATH, sign_in_complete_path)
complete.click()

time.sleep(5)

apply = driver.find_element(By.XPATH, apply_path)
apply.click()

mobile_code = driver.find_element(By.XPATH, code_path)
mobile_code.click()
india_code = driver.find_element(By.XPATH, india_path)
india_code.click()

number = driver.find_element(By.XPATH, option_path)
number.click()

number.send_keys(mobile_no)

next_1 = driver.find_element(By.XPATH, next_path)
next_1.click()

time.sleep(1)

next_1.click()

q1 = driver.find_element(By.XPATH, q1_path)
q1.click()
q1.send_keys(a1)

q2 = driver.find_element(By.XPATH, q2_path)
q2.click()
q2.send_keys(a2)

q3 = driver.find_element(By.XPATH, q3_path)
q3.click()
q3.send_keys(a3)

review = driver.find_element(By.XPATH,review_path)
review.click()

submit = driver.find_element(By.XPATH,submit_path)
submit.click()