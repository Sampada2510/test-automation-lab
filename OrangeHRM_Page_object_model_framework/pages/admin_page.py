from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
      
        # Locators
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.search_username_input = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
        self.autocomplete_option = (By.XPATH, "//div[@role='listbox']//span")  # Autocomplete dropdown suggestion
        self.search_button = (By.XPATH, "//button[@type='submit']")
        #  self.user_list_cells = (By.XPATH, "//div[@role='table']//div[@role='row']/div[2]")  # Adjusted for new table

        # New Locators for "Add" user functionality
        self.add_button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        
       # Locators on the "Add User" page (after clicking Add)
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class, 'oxd-select-text')]")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class, 'oxd-select-text')]")
        self.dropdown_option = lambda text: (By.XPATH, f"//div[@role='listbox']//span[text()='{text}']")

        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_autocomplete_option = (By.XPATH, "//div[@role='listbox']//span")

        self.username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
        self.password_input = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
        self.confirm_password_input = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")
        
        self.save_button = (By.XPATH, "//button[@type='submit']")
        #self.user_list_cells = (By.XPATH, "//table[@id='resultTable']//tr/td[2]")  # Assuming usernames are in the 2nd column

    def navigate_to_admin_page(self):
        time.sleep(5)
        self.driver.find_element(*self.admin_menu).click()

    def search_user(self, username):
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_username_input))
        input_box = self.driver.find_element(*self.search_username_input)
        input_box.clear()
        input_box.send_keys(username)

        # Wait for autocomplete and select first option
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.autocomplete_option)).click()
        time.sleep(1)

        self.driver.find_element(*self.search_button).click()
        time.sleep(3)

    def is_user_in_list(self, name_substring):
        # Wait until the page loads and text is visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Get the page content as a string
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        
        # Check if the name substring exists within the page content (case insensitive)
        if name_substring.lower() in page_text.lower():
            return True
        else:
            return False

    # New Methods for "Add User"
    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_button)).click()

     # Fill in user role, status, and employee name
    def fill_user_role_details(self, role, status, employee_name):
        # Select User Role
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.dropdown_option(role))).click()

        # Enter and select Employee Name
        emp_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.employee_name_input))
        emp_input.send_keys(employee_name)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.employee_autocomplete_option)).click()

        # Select Status
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.status_dropdown)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.dropdown_option(status))).click()

    # Fill in username, password and confirm password
    def fill_user_account_details(self, username, password, confirm_password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)


    def click_save_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button)).click()