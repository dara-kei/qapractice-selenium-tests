from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckboxesPage(BasePage):
    URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"
    BUTTON_LOCATOR = (By.ID, "submit-id-submit")
    RESULT_LOCATOR = (By.ID, "result-text")
    CHECKBOXES_CSS_SELECTOR = (By.CSS_SELECTOR, "input[type='checkbox']")
    CHECKBOXES = {"one" : (By.ID,"id_checkboxes_0"),
                  "two" : (By.ID,"id_checkboxes_1"),
                  "three" : (By.ID,"id_checkboxes_2"),}


    def count_checkboxes(self):
        return len(self.browser.find_elements(*self.CHECKBOXES_CSS_SELECTOR)) # * это распаковывает кортеж из (By.CSS_SELECTOR, "input[type='checkbox']") на 2 элемента
                                                                 # так как find_elements требует введения 2 элементов


    def get_first_checkbox_name(self):
        return self.find((By.CSS_SELECTOR,'label[for = "id_checkboxes_0"]')).text

    def get_second_checkbox_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for = "id_checkboxes_1"]')).text

    def get_third_checkbox_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for = "id_checkboxes_2"]')).text

    def check_checkbox(self, name):
        self.find(self.CHECKBOXES[name]).click()

    def checkbox_is_visible(self, name):
        return self.find(self.CHECKBOXES[name]).is_displayed()

    def checkbox_is_checked(self, name):
        return self.find(self.CHECKBOXES[name]).is_selected()

    def button_is_enabled(self):
        return self.find(self.BUTTON_LOCATOR).is_enabled()

    def get_button_name(self):
        return self.find(self.BUTTON_LOCATOR).get_attribute("value")

    def submit_button(self):
        self.find(self.BUTTON_LOCATOR).click()

    def result(self):
        return self.find(self.RESULT_LOCATOR).text

# find_elements, если нет элементов на странице, возвращает пустой список []
    def result_is_not_present(self):
        return len(self.browser.find_elements(*self.RESULT_LOCATOR)) == 0


