from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import enum


class Places(enum.Enum):
    SEA = "Sea"
    MOUNTAINS = "Mountains"
    OLD_TOWN = "Old town"
    OCEAN = "Ocean"
    RESTAURANT = "Restaurant"

class Transport(enum.Enum):
    CAR = "Car"
    BUS = "Bus"
    TRAIN = "Train"
    AIR = "Air"

class Date(enum.Enum):
    TODAY = "Today"
    TOMORROW = "Tomorrow"
    NEXT_WEEK = "Next week"


class SelectMultiple(BasePage):
    URL = "https://www.qa-practice.com/elements/select/mult_select"
    SELECT_FIELDS = {"first" : (By.ID, "id_choose_the_place_you_want_to_go"),
                     "second": (By.ID, "id_choose_how_you_want_to_get_there"),
                     "third": (By.ID, "id_choose_when_you_want_to_go")}
    BUTTON = (By.ID, "submit-id-submit")
    RESULT = (By.ID, "result-text")


    def test_loading_page(self):
        assert len(self.browser.find_elements(By.XPATH, '//select[@class="select form-select"]')) == 3
        assert self.find((By.CSS_SELECTOR, 'label[for="id_choose_the_place_you_want_to_go"]')).text == "Choose the place you want to go*"
        assert self.find((By.CSS_SELECTOR, 'label[for="id_choose_how_you_want_to_get_there"]')).text == "Choose how you want to get there*"
        assert self.find((By.CSS_SELECTOR,'label[for="id_choose_when_you_want_to_go"]')).text == "Choose when you want to go*"
        assert self.find(self.SELECT_FIELDS["first"]).get_attribute("required")
        assert self.find(self.SELECT_FIELDS["second"]).get_attribute("required")
        assert self.find(self.SELECT_FIELDS["third"]).get_attribute("required")

    def submit(self):
        self.find(self.BUTTON).click()

    def get_result_text(self):
        return self.find(self.RESULT).text

    def choose_select_option(self, select, option):
        select = Select(self.find(self.SELECT_FIELDS[select]))
        select.select_by_visible_text(option)

    def get_validation_message(self, select):
        return self.find(self.SELECT_FIELDS[select]).get_attribute("validationMessage")