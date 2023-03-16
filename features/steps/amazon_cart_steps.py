from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('I should see "Your Amazon Cart is empty"')
def verify_cart_empty(context):
    #assert "Your Amazon Cart is empty" in context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty").text
    context.app.cart_page.verify_empty_cart()


@then('I should see "Ember Temperature Control Smart Mug 2"')
def verif_ember_mug_in_cart(context):
    #assert "Ember Temperature Control Smart Mug 2" in context.driver.find_element(By.CSS_SELECTOR, "div.a-row.a-grid-vertical-align.a-grid-top.sc-list-item-content-inner").text
    context.app.cart_page.verify_black_ember_mug_in_cart()
