from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalPopupPage(BasePage):
    URL = "https://www.qa-practice.com/elements/popup/modal"
    BUTTON = (By.CSS_SELECTOR, "#content > button")
    POPUP = (By.CSS_SELECTOR, ".modal-content")
    RESULT = (By.ID, "result-text")

    @property
    def popup(self):
        return self.find(self.POPUP)

    def get_button_name(self):
        return self.find(self.BUTTON).text

    def click_button(self):
        self.find(self.BUTTON).click()

    def popup_is_visible(self):
        return self.popup.is_displayed()

    def get_popup_title(self):
        return self.popup.find_element(By.ID, "exampleModalLabel").text

    def get_checkbox_text(self):
        return self.popup.find_element(By.CSS_SELECTOR, 'label[for="id_checkbox_0"]').text

    def get_number_of_buttons(self):
        return len(self.browser.find_elements(By.CSS_SELECTOR, ".modal-footer button"))

    def get_popup_buttons_names(self):
        return [self.popup.find_element(By.CSS_SELECTOR, ".modal-footer button[type='submit']").text,
                self.popup.find_element(By.CSS_SELECTOR, ".modal-footer button[type='button']").text]

    def check_popup_checkbox(self):
        self.popup.find_element(By.ID, "id_checkbox_0").click()

    def checkbox_is_checked(self):
        return self.popup.find_element(By.ID, "id_checkbox_0").is_selected()


    def submit_popup(self):
        self.popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


    def get_text_result(self):
        return self.find(self.RESULT).text


    def cancel_popup(self):
        self.popup.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()

