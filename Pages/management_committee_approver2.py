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
driver.find_element(By.ID,"email").send_keys("DUM20670") #c
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID,"loginBtn").click()
time.sleep(2)

#-------homepage------
driver.find_element(By.XPATH,"//label[@class='switch-menu']").click()
time.sleep(2)

#--------Dashboard----------
driver.find_element(By.XPATH,"//i[@class='bi bi-file-earmark-text nav-icon']").click()
time.sleep(2)

#------under-Review--------
driver.find_element(By.XPATH,"//a[text()='Under-Review Docs']").click()
time.sleep(10)

#----------doc to be clicked--------
# driver.execute_script("window.scrollTo(1000, document.body.scrollHeight);")



# First, scroll to bottom
def scroll_to_bottom(driver, pause_time):
    pass


scroll_to_bottom(driver, pause_time=1)

# Then, wait for and find element with text '12'
element2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='12']"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element2)
driver.execute_script("arguments[0].click();", element2)
time.sleep(5)

element = driver.find_element(By.XPATH, "//a[text()='com_test6'][1]")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

#-----------scroll to end---------
element = driver.find_element(By.XPATH, "//button[text()='Approve']")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

driver.find_element(By.ID, "accept_doc").click()
time.sleep(3)

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,"acceptToProposer")))
driver.find_element(By.ID, "acceptToProposer").click()
time.sleep(5)

#acceptToApprover