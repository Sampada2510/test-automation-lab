import time
from behave import when, then
from pages.myinfo_page import MyInfoPage

@then('I navigate to the "My Info" page')
def step_navigate_to_my_info(context):
    context.myinfo_page = MyInfoPage(context.driver)
    context.myinfo_page.navigate_to_my_info()
    time.sleep(1)

@when('I update the name to "{first}" "{middle}" "{last}"')
def step_update_name(context, first, middle, last):
    context.myinfo_page.edit_user_name(first, middle, last)
    context.full_name = f"{first} {middle} {last}".strip()
    time.sleep(10)

@when('I click on the save button')
def step_click_save_button(context):
    context.myinfo_page.save_changes()
    time.sleep(2)
