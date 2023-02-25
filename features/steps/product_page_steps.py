from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Add to Cart')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    sleep(5)


@when('Close Slide Window')
def close_slide_window(context):
    context.driver.find_element(By.ID, 'attach-close_sideSheet-link').click()