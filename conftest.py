from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from pages.alert_prompt_box_page import AlertPromptBoxPage
from pages.alert_comfirmation_box_page import AlertConfirmationBoxPage
from pages.checkbox_multiple_page import CheckboxesPage
from pages.disabled_button_page import DisabledButtonPage
from pages.input_text_page import InputTextPage
from pages.simple_button_page import SimpleButtonPage
from pages.alert_box_page import AlertBoxPage
from pages.select_page import SelectPage
from pages.select_multiple_page import SelectMultiple


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--lang=en-US")

    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture()
def simple_button_page(browser):
    return SimpleButtonPage(browser)

@pytest.fixture()
def disabled_button_page(browser):
    return DisabledButtonPage(browser)

@pytest.fixture()
def input_text_page(browser):
    return InputTextPage(browser)

@pytest.fixture()
def checkboxes_page(browser):
    return CheckboxesPage(browser)

@pytest.fixture()
def alert_box_page(browser):
    return AlertBoxPage(browser)


@pytest.fixture()
def alert_confirm_page(browser):
    return AlertConfirmationBoxPage(browser)


@pytest.fixture()
def alert_prompt_page(browser):
    return AlertPromptBoxPage(browser)

@pytest.fixture()
def select_page(browser):
    return SelectPage(browser)

@pytest.fixture()
def select_multiple_page(browser):
    return SelectMultiple(browser)
