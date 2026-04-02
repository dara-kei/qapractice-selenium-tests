from pages.inputs.base_input_page import InputBasePage
from selenium.webdriver.common.by import By


class InputTextPage(InputBasePage):
    URL = 'https://www.qa-practice.com/elements/input/simple'
    TEXT_INPUT = (By.ID, 'id_text_string')
    ERROR_MESSAGE = (By.ID, 'error_1_id_text_string')

