from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Selenium driver
driver = webdriver.Chrome()

@given('I am on the surah page')
def step_impl(context):
    # Navigate to the surah page
    driver.get('https://quran.com/1')

@then('i should see a info button')
def step_impl(context):
    # Verify that the info button is present
    assert driver.find_element_by_css_selector('.btn-info')

@then('i should see a play audio button')
def step_impl(context):
    # Verify that the play audio button is present
    assert driver.find_element_by_css_selector('.btn-audio')

@then('i should see a reading button')
def step_impl(context):
    # Verify that the reading button is present
    assert driver.find_element_by_css_selector('.btn-reading')

@then('i should see a translation button')
def step_impl(context):
    # Verify that the translation button is present
    assert driver.find_element_by_css_selector('.btn-translation')

# Quit the Selenium driver after all the tests have run
def after_all(context):
    driver.quit()
