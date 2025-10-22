from select import select

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

driver =webdriver.Chrome()
driver.get("https://uc3.netiapps.net/login")

driver.maximize_window()

# -----Login Steps-------
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
driver.find_element(By.ID,"email").send_keys("DUM00877")  #DUM18090
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID,"loginBtn").click()
time.sleep(2)

#-------homepage------
driver.find_element(By.XPATH,"//label[@class='switch-menu']").click()
time.sleep(2)

#--------Dashboard----------
driver.find_element(By.XPATH,"//i[@class='bi bi-file-earmark-text nav-icon']").click()
time.sleep(2)

#--------doc assign---------
driver.find_element(By.XPATH,"//a[text()='Doc Assignment']").click()
time.sleep(2)

#------select doc to assign-------------
driver.find_element(By.XPATH, "//input[@value='617']").click()
time.sleep(5)

wait = WebDriverWait(driver, 20)

# Wait for the <select> element to be present
select_elem = wait.until(EC.presence_of_element_located((By.ID, "delegated_to")))

# Wrap the <select> element with Selenium's Select class
select = Select(select_elem)

# Select the user by value (recommended for exact match)
select.select_by_value("DUM33329") #DUM40757


select_elem1 = wait.until(EC.presence_of_element_located((By.ID, "delegation_access")))

# Wrap the <select> element with Selenium's Select class
select = Select(select_elem1)

# Select the user by value (recommended for exact match)
select.select_by_value("RA") #DUM40757



# driver.find_element(By.XPATH, "//li[@id='select2-delegated_to-result-pf68-DUM45326']").click()

#------Select Date of Death-------
# dod = WebDriverWait(driver, 2).until(
#     EC.element_to_be_clickable((By.NAME, "from_date"))
# )
#
# # Clear if any default value is present
# dod.clear()
#
# # Send the date manually (make sure format matches the site, e.g. DD-MM-YYYY or YYYY-MM-DD)
# dod.send_keys("10-09-2025")
# time.sleep(1)
#
#
# dod1 = WebDriverWait(driver, 2).until(
#     EC.element_to_be_clickable((By.NAME, "to_date"))
# )
#
# # Clear if any default value is present
# dod1.clear()
#
# # Send the date manually (make sure format matches the site, e.g. DD-MM-YYYY or YYYY-MM-DD)
# dod1.send_keys("10-09-2025")
time.sleep(7)

driver.find_element(By.XPATH, "//input[@id='delegateBtn']").click()


