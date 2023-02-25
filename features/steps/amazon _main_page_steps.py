from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop .nav-a[data-csa-c-type='link']")
BEST_SELLERS = (By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
CUSTOMER_SERVICE = (By.CSS_SELECTOR, "#nav-xshop a[href*='nav_cs_customerservice']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@when('Click on Returns&Orders')
def click_returns_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()
    sleep(3)


@when('Click on Best Sellers')
def click_on_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()
    sleep(3)


@when('Click on Customer Service')
def click_on_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()
    sleep(3)


@then('Verify hamburger menu item')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'

