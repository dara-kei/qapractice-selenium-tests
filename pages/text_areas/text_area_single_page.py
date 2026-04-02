from pages.text_areas.base_text_area_page import BaseTextAreaPage
from selenium.webdriver.common.by import By


class TextAreaSinglePage(BaseTextAreaPage):
    URL = "https://www.qa-practice.com/elements/textarea/single"
    ERROR_MESSAGE = (By.ID, "error_1_id_text_area")
    TEXT_AREA = (By.ID, "id_text_area")


    def get_text_area_name(self):
        return self.find((By.CSS_SELECTOR, f'label[for="id_text_area"]')).text

    def is_required_field(self):
        return self.find(self.TEXT_AREA).get_attribute("required") is not None


    def clear_text_area(self):
        self.find(self.TEXT_AREA).clear()


    def fill(self, text: str) -> None:
        self.find(self.TEXT_AREA).send_keys(text)

    def get_validation_message(self):
        return self.find(self.TEXT_AREA).get_attribute("validationMessage")


