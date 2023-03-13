from behave import given, when, then
from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I am on the surah page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://quran.com/1")

@then('i should see a tafsir icon')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "TranslationViewCell_icon__x_dPx")))
        context.browser.find_element(By.CLASS_NAME, "TranslationViewCell_icon__x_dPx")
        assert True
    except:
        assert False


@then('i should see a reflect icon')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Button_content__hmBjB")))
        context.browser.find_element(By.CLASS_NAME, "Button_content__hmBjB")
        assert True
    except:
        assert False


@then('i should see a ... icon')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "TranslationViewCell_icon__x_dPx")))
        context.browser.find_element(By.CLASS_NAME, "TranslationViewCell_icon__x_dPx")
        assert True
    except:
        assert False

@then('i should see a play button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Button_content__hmBjB")))
        context.browser.find_element(By.CLASS_NAME, "Button_content__hmBjB")
        assert True
    except:
        assert False

@then('i should see a juzz button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Switch_item__ePHkS Switch_itemNormal__pDPXy")))
        context.browser.find_element(By.CLASS_NAME, "Switch_item__ePHkS Switch_itemNormal__pDPXy")
        assert True
    except:
        assert False

@then('i should see a page button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Switch_item__ePHkS Switch_itemNormal__pDPXy")))
        assert context.browser.find_element(By.CLASS_NAME, "Switch_item__ePHkS Switch_itemNormal__pDPXy")
       
    except:
        assert False


@then('i should see a play audio button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Button_content__hmBjB")))
        assert context.browser.find_element(By.CLASS_NAME, "Button_content__hmBjB")
       
    except:
        assert False