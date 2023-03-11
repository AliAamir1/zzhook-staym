from selenium import webdriver
from behave import given, when, then

@given('I am on the surah page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://quran.com/surah/1")

@then('I should see a tafsir icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.tafsir-icon')

@then('I should see a reflect icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.reflect-icon')

@then('I should see a ... icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.ellipsis-icon')

@then('I should see a juzz button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.juz-btn')

@then('I should see a page button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.page-btn')

@then('I should see a surah button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.surah-btn')
