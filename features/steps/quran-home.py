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