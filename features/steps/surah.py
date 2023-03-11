from selenium import webdriver
from behave import given, when, then

@given('I am on the surah page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://quran.com/surah/1")

@then('I should see an info button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.info-icon')

@then('I should see a play audio button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.play-icon')

@then('I should see a reading button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.read-icon')

@then('I should see a translation button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.translation-icon')

@then('I should see a tafsir icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.tafsir-icon')

@then('I should see a reflect icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.reflection-icon')

@then('I should see a ... icon')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.more-icon')

@then('I should see a juzz button')
def step_impl(context):
    assert context.driver.find_element_by_css_selector('.juz-selector')


