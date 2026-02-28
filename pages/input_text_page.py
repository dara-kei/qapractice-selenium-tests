from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InputTextPage(BasePage):
    URL = 'https://www.qa-practice.com/elements/input/simple'
    INPUT_FIELD_LOCATOR = (By.ID, 'id_text_string')
    RESULT_LOCATOR = (By.ID, 'result-text')
    ERROR_MESSAGE_LOCATOR = (By.ID, 'error_1_id_text_string')


    @property
    def field(self):
        return self.find(self.INPUT_FIELD_LOCATOR)

    @property
    def result(self):
        return self.find(self.RESULT_LOCATOR)

    @property
    def error_message(self):
        return self.find(self.ERROR_MESSAGE_LOCATOR)

    def clear_field(self):
        self.field.clear()

    def input_text_in_field(self, text):
        self.field.send_keys(text)

    def press_enter(self):
        self.field.send_keys(Keys.ENTER)

    def get_validation_message(self):
        return self.field.get_attribute("validationMessage")

    def error_message_is_visible(self):
        return self.error_message.is_displayed()



