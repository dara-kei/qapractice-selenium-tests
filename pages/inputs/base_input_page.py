from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InputBasePage(BasePage):
    TEXT_INPUT = None
    RESULT_TEXT = (By.ID, "result-text")
    ERROR_MESSAGE = None

    @property
    def input(self):
        return self.find(self.TEXT_INPUT)

    def clear_input(self):
        self.input.clear()

    def input_text(self, text):
        self.input.send_keys(text)

    def press_enter(self):
        self.input.send_keys(Keys.ENTER)

    def get_validation_message(self):
        return self.input.get_attribute("validationMessage")

    def error_message_is_visible(self):
        return self.find(self.ERROR_MESSAGE).is_displayed()

    def get_text_result(self):
        return self.find(self.RESULT_TEXT).text

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text

    def text_input_is_required_field(self):
        return self.input.get_attribute("required") is not None


