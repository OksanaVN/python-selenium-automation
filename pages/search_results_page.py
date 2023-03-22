from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
    EMBER_MUG = By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/51JTZ5qwHvL._AC_UL320_.jpg']"
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_subnav_locator(self, category):
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def select_ember_black_mug(self):
        self.find_element(*self.EMBER_MUG).click()

    def verify_selected_department(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)
