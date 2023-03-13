from behave import given, when, then
from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Given step


@given('I have a web browser open')
def step_impl(context):
    context.browser = webdriver.Chrome()

# When step


@when('I open my web browser and type www.quran.com in the address bar')
def step_impl(context):
    context.browser.get("https://www.quran.com")

# Then step


@then('I should be directed to the Quran.com home page')
def step_impl(context):
    print(context.browser.current_url)
    assert context.browser.current_url == "https://quran.com/"

    # Close the browser to end the scenario
    context.browser.quit()


@given("I am on the Quran.com home page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.quran.com")


@then("search button should be there")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "Button_content__hmBjB")))
        context.browser.find_element(By.CLASS_NAME, "Button_content__hmBjB")
        assert True
    except:
        assert False, "Search button not found"


#   Scenario: check login button
#     Given I am on the Quran.com home page
#     Then login button should be there


@then("setting button should be there")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "Drawer_headerContent__iKT87")))
        context.browser.find_element(
            By.CLASS_NAME, "Drawer_headerContent__iKT87")
        assert True
    except:
        assert False, "Settings button not found"


# Scenario: check language button
#     Given I am on the Quran.com home page
#     Then language button should be there


@then("language button should be there")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "Tooltip_trigger__E263W")))
        context.browser.find_element(By.CLASS_NAME, "Tooltip_trigger__E263W")
        assert True
    except:
        assert False, "language button not found"


@then("login button should be there")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "Link_base__9W8Qs")))
        context.browser.find_element(By.CLASS_NAME, "Link_base__9W8Qs")
        assert True
    except:
        assert False, "Login  button not found"

#  Scenario: surahs are listed
#     Given that I am on quran.com home Page
#     When check for the surah div
#     Then surah are listed in the container


@then("surah are listed in the container")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "SurahPreviewRow_container__3ZfRV")))
        context.browser.find_element(
            By.CLASS_NAME, "SurahPreviewRow_container__3ZfRV")
        assert True
    except:
        assert False, "Surahs are not listed"

#  Scenario: Using the search bar
#     Given I am on Quran.com home page
#     When I click on search bar
#     Then The search pop up shows up


@when("I click on search bar")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "CommandBarTrigger_container__g1Ziu")))
        context.browser.find_element(
            By.CLASS_NAME, "CommandBarTrigger_container__g1Ziu").click()

    except:
        assert False, "Search bar testing failed"


@then("The search pop up shows up")
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "CommandBarBody_container__s5HGd")))
        assert context.browser.find_element(
            By.CLASS_NAME, "CommandBarTrigger_container__g1Ziu")
    except:
        assert False, "Search bar pop up testing failed"

#  Scenario: Accessing Quranic Surahs
#     Given I am on the search pop up
#     When I click on juz 1
#     Then I should be directed to the juz 1 page


@given("I am on the search pop up")
def step_impl(context):
    try:
        context.browser = webdriver.Chrome()
        context.browser.get("https://www.quran.com")
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, "command-bar")))
        search_bar = wait.until(EC.visibility_of_element_located((By.ID, "command-bar")))
        search_bar.click()
    except:
        assert False, "Search bar testing failed"

@when("I click on juz 1")
def step_impl(context):
    try:
       
        context.browser.get("https://quran.com/juz/1")
        assert True

    except:
        assert False, "Unable to move towards Juz 1"




@then("I should be directed to the juz 1 page")
def step_impl(context):
    try:
        #checking the surah div of sura to verify the page
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "TranslationViewCell_contentContainer__MzrKa")))
        assert context.browser.find_element(By.CLASS_NAME, "TranslationViewCell_contentContainer__MzrKa")
        
    except:
        assert False, "Unable to move towards Juz 1"
