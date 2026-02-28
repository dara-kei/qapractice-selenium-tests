from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SimpleButtonPage(BasePage):
    URL = 'https://www.qa-practice.com/elements/button/simple'
    BUTTON_LOCATOR = (By.ID, 'submit-id-submit')
    RESULT_LOCATOR = (By.ID, 'result-text')

    def __init__(self, browser):
        super().__init__(browser)


    def button(self):
        return self.find(self.BUTTON_LOCATOR)


    def button_should_be_displayed(self):
        assert self.button().is_displayed()

    def button_should_have_name(self, name):
        assert self.button().get_attribute('value') == name

    def result(self):
        return self.find(self.RESULT_LOCATOR)

    def result_should_have_text(self, text):
        assert self.result().text == text
