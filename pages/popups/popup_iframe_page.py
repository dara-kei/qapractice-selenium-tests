from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IframePopupPage(BasePage):
    URL = "https://www.qa-practice.com/elements/popup/iframe_popup"
    BUTTON_OPEN_IFRAME = (By.CSS_SELECTOR, "#content > button")
    INPUT_FORM = (By.ID, "id_text_from_iframe")
    BUTTON_SUBMIT_INPUT_FORM = (By.ID, "submit-id-submit")
    RESULT = (By.ID, "check-result")
    POP_UP_TITLE = (By.CSS_SELECTOR, "h1")
    IFRAME_TEXT_TO_COPY = (By.ID, "text-to-copy")
    IFRAME_BUTTONS = (By.CSS_SELECTOR, ".modal-footer button")
    IFRAME_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer button[type='button']")
    IFRAME_CHECK_BUTTON = (By.CSS_SELECTOR, ".modal-footer button[type='submit']")

    # def __init__(self, page: Page):
    #     super().__init__(page)
    #     self.button_open_popup = page.locator("#content > button")
    #     self.input_form = page.locator("#id_text_from_iframe")
    #     self.button_submit_input_form = page.locator("#submit-id-submit")
    #     self.result = page.locator("#check-result")
    #
    #     self.popup_title = page.frame_locator("iframe.embed-responsive-item").locator("h1")
    #     self.popup_text_to_copy = page.frame_locator("iframe.embed-responsive-item").locator("#text-to-copy")
    #
    #     self.popup_buttons = page.locator(".modal-footer button")
    #     self.popup_close_button = page.locator(".modal-footer button[type='button']")
    #     self.popup_check_button = page.locator(".modal-footer button[type='submit']")

    def get_button_open_iframe_name(self):
        return self.find(self.BUTTON_OPEN_IFRAME).text

    def open_iframe_and_switch_to_it(self):
       self.find(self.BUTTON_OPEN_IFRAME).click()
       iframe = self.find((By.CSS_SELECTOR, "iframe.embed-responsive-item"))
       self.browser.switch_to.frame(iframe)

    def get_iframe_text_to_copy(self):
        return self.find(self.IFRAME_TEXT_TO_COPY).text

    def switch_to_main_window(self):
        self.browser.switch_to.default_content()


    def get_iframe_title(self):
        return self.find(self.POP_UP_TITLE).text

    def iframe_title_is_visible(self):
        return self.find(self.POP_UP_TITLE).is_displayed()

    def get_number_of_iframe_buttons(self):
        return len(self.browser.find_elements(*self.IFRAME_BUTTONS))

    def get_iframe_buttons_names(self):
        return [self.find(self.IFRAME_CHECK_BUTTON).text, self.find(self.IFRAME_CLOSE_BUTTON).text]


    def click_check_button(self):
        self.find(self.IFRAME_CHECK_BUTTON).click()

    def click_close_button(self):
        self.find(self.IFRAME_CLOSE_BUTTON).click()

    def input_form_is_visible(self):
        return self.find(self.INPUT_FORM).is_displayed()

    def button_submit_input_form_is_visible(self):
        return self.find(self.BUTTON_SUBMIT_INPUT_FORM).is_displayed()

    def fill_input_form(self, text):
        input_form = self.find(self.INPUT_FORM)
        input_form.clear()
        input_form.send_keys(text)


    def submit_input_form(self):
        self.find(self.BUTTON_SUBMIT_INPUT_FORM).click()


    def get_result_text(self):
        return self.find(self.RESULT).text


    def get_validation_message(self):
        self.find(self.INPUT_FORM).get_attribute("validationMessage")
