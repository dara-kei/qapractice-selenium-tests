from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BaseTextAreaPage(BasePage):
    BUTTON = (By.ID, "submit-id-submit")
    RESULT = (By.ID, "result-text")
    ERROR_MESSAGE = None

    def submit(self):
        self.browser.execute_script("document.activeElement.blur();")
        self.find(self.BUTTON).click()


    def get_result_text(self):
        return self.find(self.RESULT).text


    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text
