from behave import given, when, then
from pages.leave_page import LeavePage
from datetime import datetime

@then("I navigate to the Assign Leave page")
def step_navigate_to_assign_leave(context):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.navigate_to_assign_leave()

@when('I enter the leave details for employee "{employee}" with type "{leave_type}", for today as half day "{half_day_type}", and comment "{comment}"')
def step_enter_half_day_leave_details(context, employee, leave_type, half_day_type, comment):
    today = datetime.today().strftime("%Y-%m-%d")
    context.leave_page.fill_leave_form(employee, leave_type, today, today, comment, is_half_day=True, half_day_type=half_day_type)

@when("I click on the Assign button")
def step_click_assign_button(context):
    context.leave_page.click_assign()

@then("the leave should be assigned successfully")
def step_verify_leave_assigned(context):
    assert context.leave_page.verify_success_message(), "Leave assignment failed"