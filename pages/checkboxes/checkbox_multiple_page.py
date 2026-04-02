from pages.checkboxes.base_checkboxes_page import BaseCheckboxesPage
from selenium.webdriver.common.by import By

class CheckboxesPage(BaseCheckboxesPage):
    URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"

    CHECKBOXES = {"One" : (By.ID,"id_checkboxes_0"),
                  "Two" : (By.ID,"id_checkboxes_1"),
                  "Three" : (By.ID,"id_checkboxes_2"),}


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



