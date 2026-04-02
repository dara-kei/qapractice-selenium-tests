from pages.checkboxes.base_checkboxes_page import BaseCheckboxesPage
from selenium.webdriver.common.by import By

class SingleCheckboxPage(BaseCheckboxesPage):
    URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    CHECKBOX_LOCATOR = (By.ID, "id_checkbox_0")

    @property
    def checkbox(self):
        return self.find(self.CHECKBOX_LOCATOR)

    def check_checkbox(self):
        self.checkbox.click()


    def get_checkbox_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_checkbox_0"]')).text


    def checkbox_is_checked(self):
        return self.checkbox.is_selected()

