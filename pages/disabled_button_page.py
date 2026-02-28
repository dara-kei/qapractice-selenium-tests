from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DisabledButtonPage(BasePage):
    URL = 'https://www.qa-practice.com/elements/button/disabled'
    BUTTON_LOCATOR = (By.ID, 'submit-id-submit')
    DROPDOWN_LOCATOR = (By.ID, 'id_select_state')
    RESULT_LOCATOR = (By.ID, 'result-text')

    def __init__(self, browser):
        super().__init__(browser)


    def button(self):
        return self.find(self.BUTTON_LOCATOR)

    def button_should_be_displayed(self):
        assert self.button().is_displayed()

    def button_should_have_name(self, name):
        assert self.button().get_attribute('value') == name

    def button_should_be_disabled(self):
        assert not self.button().is_enabled()

    def submit_button(self):
        self.button().click()

    def drop_down(self):
        return self.find(self.DROPDOWN_LOCATOR)

    def choose_select_option(self, option):
        select = Select(self.drop_down())
        select.select_by_visible_text(option)

    def drop_down_should_have_text(self, text):
        select = Select(self.drop_down())
        assert select.first_selected_option.text == text

    def result_should_have_text(self, text):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.text_to_be_present_in_element(self.RESULT_LOCATOR, text))



