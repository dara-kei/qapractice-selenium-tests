from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BaseCheckboxesPage(BasePage):
    CHECKBOXES_CSS_SELECTOR = (By.CSS_SELECTOR, "input[type='checkbox']")
    BUTTON_LOCATOR = (By.ID, "submit-id-submit")
    RESULT_LOCATOR = (By.ID, "result-text")


    @property
    def button(self):
        return self.find(self.BUTTON_LOCATOR)

    def button_is_visible(self):
        return self.button.is_displayed()

    def button_is_enabled(self):
        return self.button.is_enabled()

    def get_button_name(self):
        return self.button.get_attribute("value")

    def submit_button(self):
        self.button.click()

    def get_result_text(self):
        return self.find(self.RESULT_LOCATOR).text

    # find_elements, если нет элементов на странице, возвращает пустой список []
    def result_is_not_present(self):
        assert len(self.browser.find_elements(*self.RESULT_LOCATOR)) == 0

    def count_checkboxes(self):
        return len(self.browser.find_elements(*self.CHECKBOXES_CSS_SELECTOR)) # * это распаковывает кортеж из (By.CSS_SELECTOR, "input[type='checkbox']") на 2 элемента
                                                                 # так как find_elements требует введения 2 элементов