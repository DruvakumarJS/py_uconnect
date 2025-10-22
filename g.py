from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_committee_reviewer(driver, member_name):
    # Click Select2 box to open dropdown
    select2_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'select2-selection')]"))
    )
    select2_box.click()

    # Enter text in the search input box
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'select2-search__field')]"))
    )
    search_box.clear()
    search_box.send_keys(member_name)

    # Wait for options to load and click the matching option
    option_xpath = f"//li[contains(@class,'select2-results__option') and contains(text(), '{member_name}')]"
    matched_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, option_xpath))
    )
    matched_option.click()

def new_doc():
    driver = webdriver.Chrome()
    driver.get("https://uc3.netiapps.net/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    # Login steps
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("DUM24135")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "loginBtn").click()

    # Navigate homepage and dashboard
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='switch-menu']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='bi bi-file-earmark-text nav-icon']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Under-Review Docs']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' New Document / Proposal']"))).click()

    # New document creation page
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='action'][1]"))).click()

    # Select dropdowns
    Select(wait.until(EC.element_to_be_clickable((By.ID, "document_type")))).select_by_value("8")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "management_committee_list")))).select_by_value("9")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "department")))).select_by_value("19")
    # Select(wait.until(EC.element_to_be_clickable((By.ID, "sub_department")))).select_by_value("48")


    sub_dept_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "sub_department")))

    # Wait for the specific option to be present before selecting
    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='sub_department']/option[@value='48']")))

    Select(sub_dept_dropdown).select_by_value("48")

    wait = WebDriverWait(driver, 20)

    # Wait for dropdown element
    dropdown_elem = wait.until(EC.element_to_be_clickable((By.ID, "committee_recommender")))

    # Wait explicitly for the correct option with value 'DUM30592'
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='committee_recommender']/option[@value='DUM30592']")))

    # Now select by value
    Select(dropdown_elem).select_by_value("DUM30592")

    # Select(wait.until(EC.element_to_be_clickable((By.ID, "committee_recommender")))).select_by_value("DUM30592")

    # Select committee reviewer via Select2 widget
    # select_committee_reviewer(driver, "GHANSHYAMBHAI BABUBHAI - Chief Vigilance Officer")
    def select_committee_reviewer(member_name):
        # 1. Click to open Select2 dropdown
        # This is usually a <span> or sometimes input; you must inspect and choose the "Select Members" widget.
        select2_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'select2-selection')]"))
        )
        select2_box.click()

        # 2. Type in the search field
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'select2-search__field')]"))
        )
        search_box.clear()
        search_box.send_keys(member_name)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, f"//li[contains(@class,'select2-results__option') and contains(text(), '{member_name}')]"))
        )
        search_box.send_keys(Keys.ENTER)  # Or, to be robust, see next step

        # 3. Optionally, click on the exact option if multiple exist
        option_xpath = f"//li[contains(@class,'select2-results__option') and contains(text(), '{member_name}')]"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()

        # This should match the visible text or unique pattern from your <li>:
        select_committee_reviewer("GHANSHYAMBHAI BABUBHAI - Chief Vigilance Officer")

    # Fill title and upload document
    wait.until(EC.visibility_of_element_located((By.ID, "title"))).send_keys("com_test5")

    # Upload file - ensure path is correct and accessible
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='document']")))
    file_input.send_keys("/home/suraksha/Downloads/Correct_Doc.pdf.docx")

    # Scroll and click "toReview" button safely
    button_to_review = wait.until(EC.visibility_of_element_located((By.ID, "toReview")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button_to_review)
    button_to_review.click()

    # Handle SweetAlert2 popup
    swal_locator = (By.CLASS_NAME, "swal2-popup")
    wait.until(EC.visibility_of_element_located(swal_locator))

    ok_button_locator = (By.CLASS_NAME, "swal2-confirm")
    wait.until(EC.element_to_be_clickable(ok_button_locator)).click()

    # Give some time after popup before quitting
    wait.until(EC.invisibility_of_element(ok_button_locator))

    driver.quit()

new_doc()