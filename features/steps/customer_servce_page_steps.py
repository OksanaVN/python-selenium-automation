from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


C_SERVICE_HEADER_LINKS = (By.CSS_SELECTOR, "header.nav-header a")
H_CS_LINK = (By.CSS_SELECTOR, "header.nav-header div.cs-title")
H_HOME_LINK = (By.CSS_SELECTOR, "header.nav-header div.nav-item.active")
H_DIGITAL_SUPPORT_LINK = (By.CSS_SELECTOR, "header.nav-header a[href*='/gp/help/customer/display']")


@then('Verify Customer Service Header contains {cs_header_links} links')
def customer_header_links(context, cs_header_links):
    cs_header_links = int(cs_header_links)
    c_service_header_links = context.driver.find_elements(*C_SERVICE_HEADER_LINKS)
    assert len(c_service_header_links) == cs_header_links, f'Expected {cs_header_links} links, but got {len(c_service_header_links)}'


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

