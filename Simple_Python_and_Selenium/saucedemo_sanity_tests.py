import sys
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Add print statement at the beginning of the test to ensure the script starts
print("Starting the test script...")
sys.stdout.flush()  # Force the output to flush

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--chromedriver_path', required=True, help='Path to chromedriver')
parser.add_argument('--chrome_options', required=True, help='Chrome options as a string')
args = parser.parse_args()


# Set up Chrome options (headless mode for Jenkins)
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--verbose')


# Specify the path to chromedriver
chromedriver_path = 'C:\\Users\\sampa\\Downloads\\JOBS\\Projects\\SeleniumAutomation\\chromedriver.exe'

# Use the Service class to specify the path to the chromedriver
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

# Add print statement to verify the test has navigated to the page
print("Navigating to URL...")
sys.stdout.flush()  # Force the output to flush
driver.get("https://www.saucedemo.com")

# Verify Title
try:
    assert "Swag Labs" in driver.title
    print("Title matched...")
except AssertionError:
    print("Title does not match")
sys.stdout.flush()  # Force the output to flush

# Wait for username field to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

print("Navigating to the login page.................")
sys.stdout.flush()  # Force the output to flush

# Find username and password elements, and log in
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter credentials
username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()


# Verify successful login (check if the product page is displayed)
try:
    assert "Products" in driver.page_source
    print("Successfully logged in, product page loaded...")
except AssertionError:
    print("Login failed or products page not found")

sys.stdout.flush()  # Force the output to flush

# Add item to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Wait for cart to update
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))

# Verify item is added to the cart
cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert cart_count == "1", "Item was not added to the cart"
print("Successfully added item to cart.........................")
sys.stdout.flush()  # Force the output to flush

# Navigate to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Verify cart page is displayed
assert "Your Cart" in driver.page_source, "Cart page not displayed"
print("Cart page displayed successfully...")
sys.stdout.flush()  # Force the output to flush

# Quit the browser
print("Now waiting for driver to quit.......................................")
sys.stdout.flush()  # Force the output to flush
driver.quit()
