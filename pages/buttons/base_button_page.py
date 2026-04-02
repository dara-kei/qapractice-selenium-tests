from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BaseButtonPage(BasePage):
    BUTTON_LOCATOR = (By.ID, 'submit-id-submit')
    RESULT_LOCATOR = (By.ID, 'result-text')

    @property
    def button(self):
        return self.find(self.BUTTON_LOCATOR)

    def button_is_displayed(self):
        return self.button.is_displayed()

    def get_button_name(self):
        return self.button.get_attribute('value') or self.button.text

    def submit_button(self):
        self.button.click()

    def result(self):
        return self.find(self.RESULT_LOCATOR)

    def get_result_text(self):
        return self.result().text