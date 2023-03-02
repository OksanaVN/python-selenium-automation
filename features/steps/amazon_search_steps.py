from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Select "Ember Temperature Control Smart Mug"')
def select_ember_mug(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/61VXH79P8sL._AC_UL320_.jpg']").click()


@then('Verify that text {expected_result} is shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


