from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop .nav-a[data-csa-c-type='link']")
BEST_SELLERS = (By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
CUSTOMER_SERVICE = (By.CSS_SELECTOR, "#nav-xshop a[href*='nav_cs_customerservice']")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Input text {text}')
def input_search_word(context, text):
    #context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    #context.driver.find_element(*SEARCH_BUTTON).click()
    context.app.header.click_search()


@when('Click on Returns&Orders')
def click_returns_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.main_page.click_return_orders()


@when('Click on Cart')
def click_on_cart(context):
    #context.driver.find_element(By.ID, 'nav-cart-count').click()
    context.app.main_page.click_cart()


@when('Click on Best Sellers')
def click_on_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@when('Click on Customer Service')
def click_on_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@when('Click Sign In from popup')
def click_signin(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()

    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in btn not clickable'
    ).click()


@when('Wait for {sec} seconds')
def wait_for_sec(context, sec):
    sleep(int(sec))


@then('Verify hamburger menu item')
def verify_ham_menu_present(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()


@when('Click on ham menu')
def click_ham_menu(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.ham_menu.click()


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


@then('Verify sign in pop up shown')
def verify_sign_in_popup_visible(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in button not clickable'
    )


@then('Verify sign in pop up disappears')
def verify_sign_in_popup_not_visible(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_BTN),
        message='Sign in button did not disappear'
    )