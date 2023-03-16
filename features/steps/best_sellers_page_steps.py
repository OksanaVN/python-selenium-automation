from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


BEST_SELLER_LINKS = (By.CSS_SELECTOR, "#zg_header a[href*='bs_tab']")
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@then('Verify Best Seller has {best_links} links')
def verify_bestsellers_links(context, best_links):
    best_links = int(best_links)
    bestseller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(bestseller_links) == best_links, f'Expected {best_links} links, but got {len(bestseller_links)}'


@then('User can click on every link and verify correct page opens')
def click_on_every_link(context):
    top_links = context.driver.find_elements(*BEST_SELLER_LINKS)

    for i in range(len(top_links)):
        link_to_click = context.driver.find_elements(*BEST_SELLER_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'


