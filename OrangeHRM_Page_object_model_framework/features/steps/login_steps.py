import sys
import os
import time
from behave import given, when, then
from pages.login_page import LoginPage

# Add root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage

@given("I am on the OrangeHRM login page")
def step_open_login_page(context):
    if not hasattr(context, 'driver'):
        raise AttributeError("Driver is not initialized!")
    
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when("I enter valid username and password")
def step_enter_credentials(context):
    context.login_page.enter_username("Admin")
    context.login_page.enter_password("admin123")

@when("I click on the login button")
def step_click_login(context):
    context.login_page.click_login()
    time.sleep(2)  # Wait for redirect
