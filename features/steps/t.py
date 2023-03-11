from behave import given, when, then
from selenium import webdriver

@given('I am on the Google homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")

@when('I enter {keyword} into the search bar')
def step_impl(context, keyword):
    search_bar = context.driver.find_element_by_name('q')
    search_bar.send_keys(keyword)

@when('I click the search button')
def step_impl(context):
    search_button = context.driver.find_element_by_name('btnK')
    search_button.click()

@then('I should see search results for "{keyword}"')
def step_impl(context, keyword):
    assert keyword in context.driver.page_source
