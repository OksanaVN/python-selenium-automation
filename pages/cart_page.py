from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MSG = By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty"
    PRODUCT_NAME = By.CSS_SELECTOR, "div.a-row.a-grid-vertical-align.a-grid-top.sc-list-item-content-inner"

    def verify_empty_cart(self):
        assert "Your Amazon Cart is empty" in self.find_element(*self.EMPTY_CART_MSG).text, 'Cart is not empty'

    def verify_black_ember_mug_in_cart(self):
        assert "Ember Temperature Control Smart Mug 2" in self.find_element(*self.PRODUCT_NAME).text, 'No products added/Wrong product added'


