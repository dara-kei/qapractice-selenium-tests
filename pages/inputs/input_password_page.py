from pages.inputs.base_input_page import InputBasePage
from selenium.webdriver.common.by import By


class InputPasswordPage(InputBasePage):
    URL = 'https://www.qa-practice.com/elements/input/passwd'
    TEXT_INPUT = (By.ID, 'id_password')
    ERROR_MESSAGE = (By.ID, 'error_1_id_password')

