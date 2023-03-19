from behave import given, when, then
from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given("I am on the Quran.com home page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.quran.com")


@then("All the Surah tags are shown")
def step_impl(context):
    try:
        href_list = [f'/{i}' for i in range(1, 115)]
        for href_value in href_list:
            xpath = f'//a[@href="{href_value}" and @class="Link_base__9W8Qs"]'
            surah_tag = context.browser.find_element(By.XPATH, xpath)
    
      
        assert True, "All Surah Tags Present"
    except:
        assert False, "Surah Missing"


@then("View By Tab is present")
def step_impl(context):
    try:
        tabContainer = context.browser.find_element(By.CLASS_NAME, "Tabs_container__l5DHu")
        assert True, "Tab Present"
    except:
        assert False, "Tab Missing"


@when('I click Juz')
def step_impl(context):

    xpath ="//div[normalize-space()='Juz']"
    #div[contains(@class, "Tabs_tabItem__b_JVR") and contains(@class, "Tabs_tabItemSelected__Nt0wr") and text()="Juz"]'
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.presence_of_element_located(
            (By.XPATH, xpath)))
    tab_element = context.browser.find_element(By.XPATH, xpath)
    tab_element.click()

@then('I get Juz')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "JuzView_juzTitle__mVq8J")))
        context.browser.find_element(By.CLASS_NAME, "JuzView_juzTitle__mVq8J")

        assert True, "Tab Present"
    except:
        assert False, "Tab Missing"
  
@when('I switch to "{tab}"')  
def step_impl(context, tab):
    xpath = f"//div[normalize-space()='{tab}']"
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.presence_of_element_located(
            (By.XPATH, xpath)))
    tab_element = context.browser.find_element(By.XPATH, xpath)
    tab_element.click()

@then('the "{view}" is switched')
def step_impl(context, view):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, view)))
        assert True, "Tab Switched"
    except:
        assert False, "Tab Not Switched"



    

