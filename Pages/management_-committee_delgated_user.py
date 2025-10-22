from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

driver =webdriver.Chrome()
driver.get("https://uc3.netiapps.net/login")

driver.maximize_window()

# -----Login Steps-------
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
driver.find_element(By.ID,"email").send_keys("DUM33329") #DUM40757 #DUM000877
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID,"loginBtn").click()
time.sleep(5)

#----------------add signature--------------
# driver.find_element(By.ID,"okay").click()
# time.sleep(5)
# # driver.find_element(By.ID,"imageInput").click()
#
# wait = WebDriverWait(driver, 20)
#
# file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
# file_input.send_keys("/home/suraksha/Downloads/Screenshot from 2025-09-25 11-29-19.jpg")
# driver.find_element(By.XPATH,"//input[@type='submit']").click()

#-------homepage------
driver.find_element(By.XPATH,"//label[@class='switch-menu']").click()
time.sleep(2)

#--------Dashboard----------
driver.find_element(By.XPATH,"//i[@class='bi bi-file-earmark-text nav-icon']").click()
time.sleep(2)

#------under-Review--------
driver.find_element(By.XPATH,"//a[text()='Under-Review Docs']").click()
time.sleep(2)

#----------doc to be clicked--------
element = driver.find_element(By.XPATH, "//a[text()='com_test6'][1]")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("arguments[0].click();", element)
time.sleep(4)

#----------------feedback-------------
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='feedback-text']"))).send_keys("jvhvuwvbvbeu iuhvuwhvu w whgwu ryghyurghuyr")
# driver.find_element(By.XPATH,"//input[@id='addFeedbackBtn']").click()
# time.sleep(5)

#-----------scroll to end---------

#-------WHEN comment is given submit button-------
# element = driver.find_element(By.XPATH, "//button[text()='Submit Review']")
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# driver.execute_script("arguments[0].click();", element)
# time.sleep(5)



##-------WHEN no comment is given approve button-------
element = driver.find_element(By.XPATH, "//button[text()='Approve']")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

driver.find_element(By.ID, "accept_doc").click()
time.sleep(3)


#
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,"acceptToProposer")))
driver.find_element(By.ID, "acceptToProposer").click()
time.sleep(5)

#acceptToApprover