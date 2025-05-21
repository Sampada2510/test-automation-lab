from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.my_info_menu = (By.XPATH, "//span[text()='My Info']")
        self.edit_button = (By.XPATH, "//div[contains(@class,'orangehrm-edit-employee')]//button")
        self.first_name_input = (By.NAME, "firstName")
        self.middle_name_input = (By.NAME, "middleName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        #self.save_button = (By.XPATH, "//form[contains(@class, 'personal-details')]//button[@type='submit']")


    def navigate_to_my_info(self):
        self.driver.find_element(*self.my_info_menu).click()
        time.sleep(5)

    def edit_user_name(self, first_name, middle_name, last_name):
       # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.edit_button)).click()

        # Ensure the first name input field is visible and interactable
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input))

        # Clear the first name input
        self.driver.find_element(*self.first_name_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.first_name_input).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        time.sleep(2)

        # Clear the middle name input
        self.driver.find_element(*self.middle_name_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.middle_name_input).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element(*self.middle_name_input).send_keys(middle_name)
        time.sleep(2)

        # Clear the last name input
        self.driver.find_element(*self.last_name_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.last_name_input).send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        time.sleep(2)


    def save_changes(self):
        save_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.save_button)
        )

        target_button = save_buttons[0]  
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button))
        self.driver.execute_script("arguments[0].click();", target_button)

        print("Clicked the second Save button.")
        time.sleep(5)
        