from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


C_SERVICE_HEADER_LINKS = (By.CSS_SELECTOR, "header.nav-header a")
H_CS_LINK = (By.CSS_SELECTOR, "header.nav-header div.cs-title")
H_HOME_LINK = (By.CSS_SELECTOR, "header.nav-header div.nav-item.active")
H_DIGITAL_SUPPORT_LINK = (By.CSS_SELECTOR, "header.nav-header a[href*='/gp/help/customer/display']")
C_WELCOME_SECTION = (By.CSS_SELECTOR, "div.issue-card-container div.issue-card-wrapper")
LIBRARY_SEARCH = (By.ID, 'hubHelpSearchInput')


@then('Verify Customer Service Header contains {cs_header_links} links')
def customer_header_links(context, cs_header_links):
    cs_header_links = int(cs_header_links)
    c_service_h_links = context.driver.find_elements(*C_SERVICE_HEADER_LINKS)
    assert len(c_service_h_links) == cs_header_links, f'Expected {cs_header_links} links, but got {len(c_service_h_links)}'


@then('Verify Customer Service Header contain Customer Service Link')
def header_customer_service_lnk(context):
    assert "Customer Service" in context.driver.find_element(*H_CS_LINK).text


@then('Verify Customer Service Header contains Home Link')
def header_home_link(context):
    assert "Home" in context.driver.find_element(*H_HOME_LINK).text


@then('Verify Customer Service Header contains Digital Services and Device Support link')
def header_digital_support_link(context):
    assert "Digital Services and Device Support" in context.driver.find_element(*H_DIGITAL_SUPPORT_LINK).text


@then('Verify Welcome to Amazon Customer Service Header')
def cs_welcome_to_acs_header(context):
    assert "Welcome to Amazon Customer Service" in context.driver.find_element(By.CSS_SELECTOR, "div.page-container").text


@then('Verify What would you like help with today message displayed')
def what_help_you_like(context):
    assert "What would you like help with today?" in context.driver.find_element(By.CSS_SELECTOR, "p.header-subtext.subtext-container").text


@then('Verify Welcome to Amazon section contain {amount_cards} cards')
def welcome_section(context, amount_cards):
    amount_cards = int(amount_cards)
    welcome_section_cards = context.driver.find_elements(*C_WELCOME_SECTION)
    assert len(welcome_section_cards) == amount_cards, f'Expected {amount_cards} cards, but got {len(welcome_section_cards)}'


@then('Verify Search our help library header')
def search_help_library(context):
    assert "Search our help library" in context.driver.find_element(By.CSS_SELECTOR, "div.page-container h2.fs-heading.bolded").text


@then('Verify Library search input field')
def library_input_search(context):
    context.driver.find_element(*LIBRARY_SEARCH)


