from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART = By.ID, 'add-to-cart-button'
    CLOSE_SLIDE_WINDOW = By.ID, 'attach-close_sideSheet-link'

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def close_sliding_window(self):
        self.click(*self.CLOSE_SLIDE_WINDOW)
