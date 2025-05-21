from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


class LeavePage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.leave_menu = (By.XPATH, "//span[text()='Leave']")
        self.assign_leave_menu = (By.LINK_TEXT, "Assign Leave")

        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.leave_type_options = (By.XPATH, "//div[@role='listbox']//span")
        self.from_date_input = (By.XPATH, "//label[text()='From Date']/../following-sibling::div//input")
        self.to_date_input = (By.XPATH, "//label[text()='To Date']/../following-sibling::div//input")
        self.comment_box = (By.XPATH, "//textarea")
        self.duration_dropdown = (By.XPATH, "//label[text()='Duration']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.duration_options = (By.XPATH, "//div[@role='listbox']//span")
        self.assign_button = (By.XPATH, "//button[@type='submit']")
        self.success_toast = (By.XPATH, "//p[contains(text(),'Successfully Assigned')]")

    def navigate_to_assign_leave(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.leave_menu)).click()
        time.sleep(1)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave")

    def fill_leave_form(self, employee, leave_type, from_date, to_date, comment, is_half_day=False, half_day_type="AM"):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.employee_name_input)).send_keys(employee)
        time.sleep(2)  # Wait for autocomplete
        self.driver.find_element(By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{employee}')]").click()

        self.driver.find_element(*self.leave_type_dropdown).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(self.leave_type_options))
        options = self.driver.find_elements(*self.leave_type_options)
        for option in options:
            if option.text == leave_type:
                option.click()
                break

        self.driver.find_element(*self.from_date_input).clear()
        self.driver.find_element(*self.from_date_input).send_keys(from_date)
        time.sleep(2)
        self.driver.find_element(*self.to_date_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.to_date_input).send_keys(Keys.DELETE)
        self.driver.find_element(*self.to_date_input).send_keys(to_date)

        if is_half_day:
            self.driver.find_element(*self.duration_dropdown).click()
            time.sleep(1)
            duration_options = self.driver.find_elements(*self.duration_options)
            for opt in duration_options:
                if "Half Day" in opt.text:
                    opt.click()
                    break

            # Select AM or PM after Half Day
            time.sleep(1)
            half_day_dropdown = self.driver.find_elements(By.XPATH, "//div[contains(@class,'oxd-select-text')]")[-1]
            half_day_dropdown.click()
            time.sleep(1)
            half_day_options = self.driver.find_elements(*self.duration_options)
            for option in half_day_options:
                if half_day_type.upper() in option.text:
                    option.click()
                    break

        self.driver.find_element(*self.comment_box).send_keys(comment)

    def click_assign(self):
        self.driver.find_element(*self.assign_button).click()
        time.sleep(2)
        # Wait for the confirmation popup and click OK
        try:
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'orangehrm-button-margin') and normalize-space()='Ok']"))
            )
            ok_button.click()
        except Exception as e:
            print("Confirmation box not found or OK button not clickable:", e)

        time.sleep(2)  

    def verify_success_message(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.success_toast)
            )
            return True
        except:
            return False