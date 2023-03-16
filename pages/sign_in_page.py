from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_email_field(self):
        assert self.find_element(*self.EMAIL_FIELD).is_displayed(), 'Email field not shown'
