from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.selects.base_select_page import BaseSelectPage


class SelectSinglePage(BaseSelectPage):
    URL = "https://www.qa-practice.com/elements/select/single_select"
    SELECT = (By.ID, "id_choose_language")
    LABEL_SELECT = (By.CSS_SELECTOR, "label[for='id_choose_language']")


    def choose_select_option(self, option: str) -> None:
        select = Select(self.select)
        select.select_by_visible_text(option)

    def get_validation_message(self):
        return self.select.get_attribute("validationMessage")

    def select_is_required(self):
        return self.select.get_attribute("required") is not None

    def select_is_named(self) -> None:
        return self.find(self.LABEL_SELECT).text



