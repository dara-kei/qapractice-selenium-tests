from pages.buttons.base_button_page import BaseButtonPage
from selenium.webdriver.common.by import By

class LooksLikeAButtonPage(BaseButtonPage):
    URL = 'https://www.qa-practice.com/elements/button/like_a_button'
    BUTTON_LOCATOR = (By.CSS_SELECTOR, '.a-button')
