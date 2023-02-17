from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Returns&Orders')
def click_returns_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify Sign in Page by finding Email input field')
def verify_email_input_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()
    sleep(3)


@then('I should see "Your Amazon Cart is empty"')
def verify_cart_empty(context):
    assert "Your Amazon Cart is empty" in context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty").text


@when('Select "Ember Temperature Control Smart Mug"')
def select_ember_mug(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/61VXH79P8sL._AC_UL320_.jpg']").click()


@when('Click on Add to Cart')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    sleep(5)


@when('Close Slide Window')
def close_slide_window(context):
    context.driver.find_element(By.ID, 'attach-close_sideSheet-link').click()


@then('I should see "Ember Temperature Control Smart Mug 2"')
def verif_ember_mug_in_cart(context):
    assert "Ember Temperature Control Smart Mug 2" in context.driver.find_element(By.CSS_SELECTOR, "div.a-row.a-grid-vertical-align.a-grid-top.sc-list-item-content-inner").text


