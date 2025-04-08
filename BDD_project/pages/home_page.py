from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://awesomeqa.com/ui/"

    def go_to_homepage(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def search_product(self, product_name):
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.clear()
        search_input.send_keys(product_name + Keys.RETURN)
        time.sleep(2)

    def is_product_in_results(self, product_name):
        results = self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb h4 a")
        return any(product_name in item.text for item in results)

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
        for product in products:
            title = product.find_element(By.CSS_SELECTOR, "h4 a").text
            if product_name in title:
                product.find_element(By.XPATH, ".//button[@onclick and contains(@onclick,'cart')]").click()
                time.sleep(2)
                break

    def is_success_message_shown(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").is_displayed()

    def click_contact_us(self):
        self.driver.find_element(By.LINK_TEXT, "Contact Us").click()
