from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import enum


class ProgrammingLanguage(enum.Enum):

    # с помощью enum создаем перечисление ProgrammingLanguage, в котором:
    # PYTHON — это имя элемента
    # "Python" — его значение

    # ProgrammingLanguage.PYTHON - это объект enum, у которого:
    # ProgrammingLanguage.PYTHON.name   # "PYTHON"
    # ProgrammingLanguage.PYTHON.value  # "Python"


    PYTHON = "Python"
    JAVASCRIPT = "JavaScript"
    JAVA = "Java"
    RUBY = "Ruby"
    SHARP = "C#"


class SelectPage(BasePage):
    URL = "https://www.qa-practice.com/elements/select/single_select"
    SELECT = (By.ID, "id_choose_language")
    BUTTON = (By.ID, "submit-id-submit")
    RESULT = (By.ID, "result-text")
    LABEL_SELECT = (By.CSS_SELECTOR, "label[for='id_choose_language']")


    @property
    def select(self):
        return self.find(self.SELECT)

    def submit(self):
        self.find(self.BUTTON).click()

    def choose_select_option(self, option: str) -> None:
        select = Select(self.select)
        select.select_by_visible_text(option)

    def get_result_text(self) -> None:
        return self.find(self.RESULT).text

    def get_validation_message(self):
        return self.select.get_attribute("validationMessage")

    def select_is_required(self):
        return self.select.get_attribute("required")

    def select_is_named(self) -> None:
        return self.find(self.LABEL_SELECT).text


