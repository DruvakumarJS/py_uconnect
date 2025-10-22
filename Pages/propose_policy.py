from select import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.common.devtools.v139.dom import move_to, scroll_into_view_if_needed
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.fed_cm import click_dialog_button
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

#selenium.webdriver.support.ui
driver =webdriver.Chrome()
driver.get("https://uc3.netiapps.net/login")

driver.maximize_window()

# -----Login Steps-------
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
driver.find_element(By.ID,"email").send_keys("DUM07858")
driver.find_element(By.ID, "password").send_keys("123456789")
driver.find_element(By.ID,"loginBtn").click()
time.sleep(4)

#-------homepage------
driver.find_element(By.XPATH,"//label[@class='switch-menu']").click()
time.sleep(4)

#--------Dashboard----------
driver.find_element(By.XPATH,"//i[@class='bi bi-file-earmark-text nav-icon']").click()
time.sleep(3)

#------under-Review--------
driver.find_element(By.XPATH,"//a[text()='Under-Review Docs']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[text()=' New Document / Proposal']").click()
time.sleep(6)

#---------new Document creation page---------
def new_doc():
    driver.find_element(By.XPATH,"//input[@id='action'][1]").click()
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='document_type']")
    sel_obj = Select(dropdown_element)
    sel_obj.select_by_value("3")
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='department']")
    sel_obj1 = Select(dropdown_element)
    sel_obj1.select_by_value("12")
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='sub_department']")
    sel_obj2 = Select(dropdown_element)
    sel_obj2.select_by_value("28")
    time.sleep(5)

    #driver.find_element(By.XPATH, "//input[text()='Regulatory']").click()
    # time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='policy']")
    sel_obj3 = Select(dropdown_element)
    sel_obj3.select_by_value("26")
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='management_committee_list_policy']")
    sel_obj4 = Select(dropdown_element)
    sel_obj4.select_by_value("7")
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='recommender_list_policy']")
    sel_obj5 = Select(dropdown_element)
    sel_obj5.select_by_value("DUM06593")
    time.sleep(5)

    dropdown_element = driver.find_element(By.XPATH, "//select[@id='policy_compliance_list']")
    sel_obj5 = Select(dropdown_element)
    sel_obj5.select_by_value("DUM20670")
    time.sleep(5)

    driver.find_element(By.XPATH,"//input[@name='document']").send_keys("/home/suraksha/Downloads/Correct_Doc.pdf.docx")
    time.sleep(10)


    scroll_into_view_if_needed()


    driver.find_element(By.ID, "toDroft").click()
    time.sleep(10)

    # Handle SweetAlert2 popup
    # yes_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//button[text()='Yes, save as draft']"))
    # )
    # driver.execute_script("arguments[0].scrollIntoView(true);", yes_button)
    #yes_button.click()

    swal_locator = (By.CLASS_NAME, "swal2-popup")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(swal_locator))

    # Get Swal message
    ok_button_locator = (By.CLASS_NAME, "swal2-confirm")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ok_button_locator)).click()
    time.sleep(3)
new_doc()