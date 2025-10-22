from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def test_login(_drivers):
    driver = webdriver.Chrome()
    driver.get("https://uc3.netiapps.net/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    # Login steps
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("DUM24135")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "loginBtn").click()

@pytest.mark.dependency(depends=["test_login"])
def test_NgoCreate(_drivers,request):
    ngo_page = NgoCreatePage(_drivers)
