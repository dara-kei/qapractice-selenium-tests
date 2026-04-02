from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.selects.base_select_page import BaseSelectPage


class SelectMultiple(BaseSelectPage):
    URL = "https://www.qa-practice.com/elements/select/mult_select"
    SELECT_FIELDS = {"first": (By.ID, "id_choose_the_place_you_want_to_go"),
                     "second": (By.ID, "id_choose_how_you_want_to_get_there"),
                     "third": (By.ID, "id_choose_when_you_want_to_go")}

    def count_selects(self):
        return len(self.browser.find_elements(By.XPATH, '//select[@class="select form-select"]'))

    def get_first_select_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_choose_the_place_you_want_to_go"]')).text

    def get_second_select_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_choose_how_you_want_to_get_there"]')).text

    def get_third_select_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_choose_when_you_want_to_go"]')).text

    def first_select_is_required(self):
        return self.find(self.SELECT_FIELDS["first"]).get_attribute("required") is not None

    def second_select_is_required(self):
        return self.find(self.SELECT_FIELDS["second"]).get_attribute("required") is not None

    def third_select_is_required(self):
        return self.find(self.SELECT_FIELDS["third"]).get_attribute("required") is not None

    def choose_select_option(self, select, option):
        select = Select(self.find(self.SELECT_FIELDS[select]))
        select.select_by_visible_text(option)

    def get_validation_message(self, select):
        return self.find(self.SELECT_FIELDS[select]).get_attribute("validationMessage")