from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    RETURN_ORDERS = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count')

    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def click_return_orders(self):
        self.click(*self.RETURN_ORDERS)

    def click_cart(self):
        self.click(*self.CART)

