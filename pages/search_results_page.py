from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
    EMBER_MUG = By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/51JTZ5qwHvL._AC_UL320_.jpg']"

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def select_ember_black_mug(self):
        self.find_element(*self.EMBER_MUG).click()
