from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign in Page by finding Email input field')
def verify_email_input_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'




