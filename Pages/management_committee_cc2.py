from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def select_committee_reviewer(driver, member_name):
    wait = WebDriverWait(driver, 20)

    try:
        print("🔍 Opening Select2 dropdown...")

        # Step 1: Click the visible select2 box (not the open one)
        select2_container = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@id,'select2-committee_reviewer_list_ops-container')]")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", select2_container)
        driver.execute_script("arguments[0].click();", select2_container)
        time.sleep(1)

        print("✅ Dropdown opened. Searching for reviewer...")

        # Step 2: Type into the search field
        search_box = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[contains(@class,'select2-search__field')]"))
        )
        search_box.clear()
        search_box.send_keys(member_name)
        time.sleep(1.5)

        # Step 3: Select from results
        option_xpath = f"//li[contains(@class,'select2-results__option') and contains(text(), '{member_name}')]"
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        driver.execute_script("arguments[0].click();", option)

        print(f"✅ Successfully selected reviewer: {member_name}")

    except TimeoutException:
        print(f"❌ Timeout: Could not find or select reviewer '{member_name}'")
        driver.save_screenshot("select2_timeout.png")

    except Exception as e:
        print(f"⚠️ Unexpected error selecting reviewer '{member_name}': {e}")






#     search_box.clear()
#     search_box.send_keys(member_name)
#
#     # Wait for options visible with partial text match
#     #option_xpath = f"//li[contains(@class,'select2-results__option') and contains(text(), '{member_name}')]"
#
#     #3
#     options = wait.until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "//li[contains(@class,'select2-selection__choice__display') and contains(text(), '{member_name}')]")
#       )
#     )
#
#
#     option_texts = [opt.text for opt in options]
#     print("Available options:", option_texts)
#
#     # 4. Validate the desired option is present
#     matching_options = [opt for opt in options if member_name in opt.text]
#     if not matching_options:
#         raise Exception(f"Option with name '{member_name}' not found in Select2 dropdown!")
#
#     # 5. Click the matching option
#     option_to_click = matching_options[0]
#     actions = ActionChains(driver)
#     actions.move_to_element(option_to_click).click().perform()
#
#
# # Usage example
# # Suppose this is the xpath for the reviewer Select2 container (adjust as needed):
# dropdown_xpath = "//span[contains(@class, 'select2-selection') and contains(@class, 'select2-selection--multiple') and contains(@class, 'select2-selection--clearable')]"
#     #option.click()

# driver.save_screenshot("after_click.png")


def new_doc():
    driver = webdriver.Chrome()
    driver.get("https://uc3.netiapps.net/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    # Login steps
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("DUM39995")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "loginBtn").click()

    # Navigation
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='switch-menu']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='bi bi-file-earmark-text nav-icon']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Under-Review Docs']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' New Document / Proposal']"))).click()

    # New doc page - select action
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='action'][1]"))).click()

    # Select dropdowns
    Select(wait.until(EC.element_to_be_clickable((By.ID, "document_type")))).select_by_value("8")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "management_committee_list")))).select_by_value("2")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "department")))).select_by_value("6")

    #sub-department
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//select[@id='sub_department']/option[@value='9']")))
    Select(wait.until(EC.element_to_be_clickable((By.ID, "sub_department")))).select_by_value("9")

    #recommender
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//select[@id='committee_recommender']/option[@value='DUM42711']")))
    Select(wait.until(EC.element_to_be_clickable((By.ID, "committee_recommender")))).select_by_value("DUM42711")

    #First reviewer
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//select[@id='committee_reviewer_list']/option[@value='DUM22973']")))
    Select(wait.until(EC.element_to_be_clickable((By.ID, "committee_reviewer_list")))).select_by_value("DUM22973")

    #second Reviewer
    select_committee_reviewer(driver, "RAFIQ NORMOHAMMAD - Deputy-Chief Financial Officer")


    # Fill title
    wait.until(EC.visibility_of_element_located((By.ID, "title"))).send_keys("com_test6")

    # Upload file
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='document']")))
    file_input.send_keys("/home/suraksha/Downloads/Correct_Doc.pdf.docx")

    # Wait a little for file processing, then scroll to submit button and click
    time.sleep(5)  # Adjust if necessary depending on load time

    # Scroll to and click submit button (#toReview)
    button_to_review = wait.until(EC.element_to_be_clickable((By.ID, "toReview")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button_to_review)
    time.sleep(6)  # optional small pause to allow scroll position to settle
    driver.execute_script("arguments[0].click();", button_to_review)

    # Handle SweetAlert2 popup
    swal_locator = (By.CLASS_NAME, "swal2-popup")
    wait.until(EC.visibility_of_element_located(swal_locator))
    time.sleep(5)
    ok_button_locator = (By.CLASS_NAME, "swal2-confirm")
    wait.until(EC.element_to_be_clickable(ok_button_locator)).click()
    wait.until(EC.invisibility_of_element(ok_button_locator))
    time.sleep(8)

    # Quit driver
    driver.quit()

new_doc()
