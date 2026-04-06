from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from pages.alerts.alert_prompt_box_page import AlertPromptBoxPage
from pages.alerts.alert_comfirmation_box_page import AlertConfirmationBoxPage
from pages.checkboxes.checkbox_multiple_page import CheckboxesPage
from pages.checkboxes.single_checkbox_page import SingleCheckboxPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.disabled_button_page import DisabledButtonPage
from pages.buttons.looks_like_a_button_page import LooksLikeAButtonPage
from pages.inputs.input_text_page import InputTextPage
from pages.inputs.input_email_page import InputEmailPage
from pages.inputs.input_password_page import InputPasswordPage

from pages.alerts.alert_box_page import AlertBoxPage
from pages.selects.select_single_page import SelectSinglePage
from pages.selects.select_multiple_page import SelectMultiple
from pages.text_areas.text_area_single_page import TextAreaSinglePage
from pages.text_areas.text_area_multiple_page import TextAreasMultiplePage
from pages.drag_and_drop.drag_and_drop_boxes_page import DragAndDropBoxesPage
from pages.drag_and_drop.drag_and_drop_image_page import DragAndDropImagePage
from pages.new_tabs.new_tab_with_button_page import NewTabWithButtonPage
from pages.new_tabs.new_tab_with_link_page import NewTabLinkPage
from pages.popups.popup_modal_page import ModalPopupPage
from pages.popups.popup_iframe_page import IframePopupPage


@pytest.fixture(scope="function")
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
def looks_like_button_page(browser):
    return LooksLikeAButtonPage(browser)

@pytest.fixture()
def disabled_button_page(browser):
    return DisabledButtonPage(browser)

@pytest.fixture()
def input_text_page(browser):
    return InputTextPage(browser)

@pytest.fixture()
def input_email_page(browser):
    return InputEmailPage(browser)

@pytest.fixture()
def input_password_page(browser):
    return InputPasswordPage(browser)

@pytest.fixture()
def checkbox_single_page(browser):
    return SingleCheckboxPage(browser)


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
def select_single_page(browser):
    return SelectSinglePage(browser)

@pytest.fixture()
def select_multiple_page(browser):
    return SelectMultiple(browser)


@pytest.fixture()
def text_area_single_page(browser):
    return TextAreaSinglePage(browser)


@pytest.fixture()
def text_areas_multiple_page(browser):
    return TextAreasMultiplePage(browser)

@pytest.fixture()
def drag_and_drop_boxes_page(browser):
    return DragAndDropBoxesPage(browser)

@pytest.fixture()
def drag_and_drop_image_page(browser):
    return DragAndDropImagePage(browser)


@pytest.fixture()
def new_tab_with_button_page(browser):
    return NewTabWithButtonPage(browser)

@pytest.fixture()
def new_tab_with_link_page(browser):
    return NewTabLinkPage(browser)

@pytest.fixture()
def popup_modal_page(browser):
    return ModalPopupPage(browser)

@pytest.fixture()
def popup_iframe_page(browser):
    return IframePopupPage(browser)