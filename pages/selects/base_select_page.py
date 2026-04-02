from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BaseSelectPage(BasePage):
    SELECT = None
    BUTTON = (By.ID, "submit-id-submit")
    RESULT = (By.ID, "result-text")


    @property
    def select(self):
        return self.find(self.SELECT)

    def submit(self):
        self.find(self.BUTTON).click()

    def get_result_text(self) -> None:
        return self.find(self.RESULT).text






