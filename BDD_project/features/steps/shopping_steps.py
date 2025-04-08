from behave import given, when, then
from selenium import webdriver
from pages.home_page import HomePage

@given("the user is on the homepage")
def step_homepage(context):
    context.driver = webdriver.Chrome()
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_homepage()

@when('the user searches for "MacBook"')
def step_search_product(context):
    context.home_page.search_product("MacBook")

@then('the search results should show the product "MacBook"')
def step_check_search_results(context):
    assert context.home_page.is_product_in_results("MacBook")
    context.driver.quit()

@given('the user searched for "MacBook"')
def step_search_product_given(context):
    context.driver = webdriver.Chrome()
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_homepage()
    context.home_page.search_product("MacBook")

@when("the user adds the product to the cart")
def step_add_product_to_cart(context):
    context.home_page.add_product_to_cart("MacBook")

@then("the success message should confirm the product is added")
def step_cart_success(context):
    assert context.home_page.is_success_message_shown()
    context.driver.quit()

@when('the user clicks on "Contact Us"')
def step_click_contact(context):
    context.home_page.click_contact_us()

@then("the contact page should be displayed")
def step_contact_page(context):
    assert "contact" in context.driver.current_url.lower()
    context.driver.quit()
