from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


DOG_IMG = (By.CSS_SELECTOR, '#d')


@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on a dog image')
def click_image(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])
    #
    # context.current_window = context.driver.current_window_handle


@then('Verify blog is opened')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
