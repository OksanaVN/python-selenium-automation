from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BEST_SELLER_LINKS = (By.CSS_SELECTOR, "#zg_header a[href*='bs_tab']")


@then('Verify Best Seller has {best_links} links')
def verify_bestsellers_links(context, best_links):
    best_links = int(best_links)
    bestseller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(bestseller_links) == best_links, f'Expected {best_links} links, but got {len(bestseller_links)}'


