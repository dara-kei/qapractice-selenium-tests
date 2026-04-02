from pages.inputs.base_input_page import InputBasePage
from selenium.webdriver.common.by import By


class InputEmailPage(InputBasePage):
    URL = 'https://www.qa-practice.com/elements/input/email'
    TEXT_INPUT = (By.ID, 'id_email')
    ERROR_MESSAGE = (By.ID, 'error_1_id_email')
