from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://uc3.netiapps.net/login")

driver.maximize_window()

# -----Login Steps-------
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys("DUM30592")
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(4)

# -------homepage------
driver.find_element(By.XPATH, "//label[@class='switch-menu']").click()
time.sleep(4)

# --------Dashboard----------
driver.find_element(By.XPATH, "//i[@class='bi bi-file-earmark-text nav-icon']").click()
time.sleep(3)

# ------under-Review--------
driver.find_element(By.XPATH, "//a[text()='Under-Review Docs']").click()
time.sleep(5)

# ---------Policies tab--------
# driver.find_element(By.XPATH, "(//button[contains(@class, 'nav-link') and contains(@class, 'show') and contains(@class, 'active')])[2]").click()
# time.sleep(3)

# Scroll to bottom of page to make elements clickable
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)

# --------policy selection--------
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//tbody/tr[4]/th[2]/div[1]/div[1]/a[1]')))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
time.sleep(1)
try:
    element.click()
except Exception:
    driver.execute_script("arguments[0].click();", element)

# Click Approve button at bottom of page
element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Approve']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element1)
time.sleep(1)
try:
    element1.click()
except Exception:
    driver.execute_script("arguments[0].click();", element1)

driver.quit()
