from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Selenium driver
driver = webdriver.Chrome()

@given('setting menu is oppened')
def step_impl(context):
    # Navigate to the quran.com homepage
    driver.get('https://quran.com/')

    # Find the settings menu button and click it
    settings_button = driver.find_element_by_css_selector('.menu-icon')
    settings_button.click()

@when('I click on font size - button')
def step_impl(context):
    # Find the font size button and click it
    font_size_button = driver.find_element_by_css_selector('.decrease-font-size')
    font_size_button.click()

@then('Font size will decrease')
def step_impl(context):
    # Verify that the font size has decreased
    font_size = driver.find_element_by_css_selector('.verse-container').value_of_css_property('font-size')
    assert font_size == '18px'

@when('I click on the check box of transliteration')
def step_impl(context):
    # Find the transliteration checkbox and click it
    transliteration_checkbox = driver.find_element_by_css_selector('#transliteration-toggle')
    transliteration_checkbox.click()

@then('transliteration will get enabled')
def step_impl(context):
    # Verify that transliteration is now enabled
    assert driver.find_element_by_css_selector('.translation').text.startswith('In the name of Allah')

@when('I click on the check box of translation tt')
def step_impl(context):
    # Find the translation checkbox and click it
    translation_checkbox = driver.find_element_by_css_selector('#translation-toggle')
    translation_checkbox.click()

@then('translation will get deactivated tt')
def step_impl(context):
    # Verify that translation is now deactivated
    assert not driver.find_elements_by_css_selector('.translation')

@when('I click on the check box of translation wbw')
def step_impl(context):
    # Find the translation checkbox and click it
    translation_checkbox = driver.find_element_by_css_selector('#wbw-toggle')
    translation_checkbox.click()

@then('translation will get deactivated wbw')
def step_impl(context):
    # Verify that translation is now deactivated
    assert not driver.find_elements_by_css_selector('.translation')

@when('I click on the auto scroll button')
def step_impl(context):
    # Find the auto scroll button and click it
    auto_scroll_button = driver.find_element_by_css_selector('.autoscroll-toggle')
    auto_scroll_button.click()

@then('Auto scroll will get disabled')
def step_impl(context):
    # Verify that auto scroll is now disabled
    assert not driver.find_elements_by_css_selector('.autoscroll')

@given('I am on quran.com home page')
def step_impl(context):
    # Navigate to the quran.com homepage
    driver.get('https://quran.com/')

@when('I click on surah fatiha')
def step_impl(context):
    # Find the surah fatiha link and click it
    surah_fatiha_link = driver.find_element_by_css_selector('a[href="/1"]')
    surah_fatiha_link.click()

@then('I will enter on surah faitha page')
def step_impl(context):
    # Verify that we are now on the surah fatiha page
    assert driver.current_url == 'https://quran.com/1'
    
# Quit the Selenium driver after all the tests have run
def after_all(context):
    driver.quit()
