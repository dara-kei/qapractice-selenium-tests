from pages.alert_base_page import AlertBasePage


class AlertPromptBoxPage(AlertBasePage):
    URL = 'https://www.qa-practice.com/elements/alert/prompt'

    def fill_text(self, text):
        alert = self.wait_for_alert()
        alert.send_keys(text)

