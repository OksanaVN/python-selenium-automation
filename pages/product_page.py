from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART = By.ID, 'add-to-cart-button'
    CLOSE_SLIDE_WINDOW = By.ID, 'attach-close_sideSheet-link'
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals']")
    WOMEN_LINK = (By.CSS_SELECTOR, "a[href*='/s?i=fashion-womens']")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def close_sliding_window(self):
        self.click(*self.CLOSE_SLIDE_WINDOW)

    def hover_over_new_arrival(self):
        new_arrival = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival)
        actions.perform()

    def verify_women_link(self):
        self.wait_for_element_appear(*self.WOMEN_LINK)

