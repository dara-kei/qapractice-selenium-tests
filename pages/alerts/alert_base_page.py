from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertBasePage(BasePage):

    BUTTON = (By.CSS_SELECTOR, ".a-button")
    RESULT = (By.ID, 'result-text')

    @property
    def button(self):
        return self.find(self.BUTTON)

    def button_is_visible(self):
        return self.button.is_displayed()

    def click_button(self):
        self.button.click()

    def wait_for_alert(self, timeout=5):
        return WebDriverWait(self.browser, timeout).until(
            EC.alert_is_present()
        )

    def get_alert_text(self):
        alert = self.wait_for_alert()
        return alert.text

    def alert_accept(self):
        alert = self.wait_for_alert()
        alert.accept()

    def alert_cancel(self):
        alert = self.wait_for_alert()
        alert.dismiss()

    def get_result_text(self):
        return self.find(self.RESULT).text