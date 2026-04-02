from pages.buttons.base_button_page import BaseButtonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DisabledButtonPage(BaseButtonPage):
    URL = 'https://www.qa-practice.com/elements/button/disabled'
    DROPDOWN_LOCATOR = (By.ID, 'id_select_state')


    def button_is_enabled(self):
        return self.button.is_enabled()

    def drop_down(self):
        return self.find(self.DROPDOWN_LOCATOR)

    def choose_select_option(self, option):
        select = Select(self.drop_down())
        select.select_by_visible_text(option)

    def get_drop_down_text(self):
        select = Select(self.drop_down())
        return select.first_selected_option.text





