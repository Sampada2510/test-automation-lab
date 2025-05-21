from behave import given, when, then
from pages.admin_page import AdminPage
import time

@given("I am logged in as an admin user")
def step_logged_in_as_admin(context):
    # Assuming login is done in a separate feature or step file
    # Use context to access logged-in session or login flow here
    assert hasattr(context, 'driver'), "Driver not initialized"
    assert context.driver is not None, "Driver is not initialized"
    context.admin_page = AdminPage(context.driver)
    time.sleep(2)

@then("I navigate to the Admin page")
def step_navigate_to_admin_page(context):
    context.admin_page.navigate_to_admin_page()

@when('I search for the username "{username}"')
def step_search_for_username(context, username):
    context.admin_page.search_user(username)
    time.sleep(2)  # Add wait time to ensure search results load

# New steps for adding a user
@when("I click on the Add button")
def step_click_add_button(context):
    context.admin_page.click_add_button()

@when('I fill in the userrole "{role}", status "{status}", and employeename "{employee_name}"')
def step_fill_user_role_details(context, role, status, employee_name):
    context.admin_page.fill_user_role_details(role, status, employee_name)
    time.sleep(1)

@when('I fill in the user details with username "{username}", password "{password}" and confirm password "{confirm_password}"')
def step_fill_user_account_details(context, username, password, confirm_password):
    context.admin_page.fill_user_account_details(username, password, confirm_password)
    time.sleep(1)

@when("I click on the Save button on add user")
def step_click_save_button(context):
    context.admin_page.click_save_button()


@then('the user "{username}" should be visible in the result')
def step_check_if_user_is_visible(context, username):
    assert context.admin_page.is_user_in_list(username), f"User {username} not found in the admin user list"

