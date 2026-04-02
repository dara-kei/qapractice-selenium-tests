from pages.text_areas.base_text_area_page import BaseTextAreaPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TextAreasMultiplePage(BaseTextAreaPage):
    URL = "https://www.qa-practice.com/elements/textarea/textareas"
    ERROR_MESSAGE = (By.ID, "error_1_id_first_chapter")
    TEXT_AREAS = [(By.ID, "id_first_chapter"),
                       (By.ID, "id_second_chapter"),
                       (By.ID, "id_third_chapter")]

    def hover_over_the_button(self):
        actions = ActionChains(self.browser)
        actions.move_to_element(self.find(self.BUTTON)).perform()


    def fill_areas(self, first = None, second = None, third = None):
        if first is not None:
            el = self.find(self.TEXT_AREAS[0])
            el.clear()
            el.send_keys(first)

        if second is not None:
            el = self.find(self.TEXT_AREAS[1])
            el.clear()
            el.send_keys(second)
        if third is not None:
            el = self.find(self.TEXT_AREAS[2])
            el.clear()
            el.send_keys(third)

    def clear_text_area(self, text_area_number: int):
        self.find(self.TEXT_AREAS[text_area_number]).clear()

    def count_text_areas(self):
        return len(self.browser.find_elements(By.CSS_SELECTOR, ".textarea.form-control"))


    def get_first_text_area_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_first_chapter"]')).text

    def get_second_text_area_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_second_chapter"]')).text

    def get_third_text_area_name(self):
        return self.find((By.CSS_SELECTOR, 'label[for="id_third_chapter"]')).text


    def first_area_is_required(self):
        return self.find(self.TEXT_AREAS[0]).get_attribute("required") is not None

    def get_validation_message(self, text_area_number: int):
        return self.find(self.TEXT_AREAS[text_area_number]).get_attribute("validationMessage")

