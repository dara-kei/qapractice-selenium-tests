import pytest


@pytest.mark.positive

def test_name_of_button_that_open_popup(popup_iframe_page):
    popup_iframe_page.open()
    assert popup_iframe_page.get_button_open_iframe_name() == "Launch Pop-Up"


@pytest.mark.positive
@pytest.mark.xfail(reason="Bug: wrong name for a button", strict=False)
def test_popup_initial_state(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_iframe_and_switch_to_it()
    assert popup_iframe_page.iframe_title_is_visible()
    assert popup_iframe_page.get_iframe_title() == "Iframe page title"
    assert popup_iframe_page.get_text_to_copy() == "I am the text you want to copy"
    popup_iframe_page.switch_to_main_window()
    assert popup_iframe_page.get_number_of_iframe_buttons() == 2
    assert popup_iframe_page.get_iframe_buttons_names()[0] == "Check"
    assert popup_iframe_page.get_iframe_buttons_names()[1] == "Cancel"



@pytest.mark.positive
def test_input_form_initial_state(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_iframe_and_switch_to_it()
    popup_iframe_page.switch_to_main_window()
    popup_iframe_page.click_check_button()
    assert popup_iframe_page.input_form_is_visible()
    assert popup_iframe_page.button_submit_input_form_is_visible()


@pytest.mark.positive
def test_submit_input_form_with_valid_data(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_iframe_and_switch_to_it()
    text_to_copy = popup_iframe_page.get_iframe_text_to_copy()
    popup_iframe_page.switch_to_main_window()
    popup_iframe_page.click_check_button()
    popup_iframe_page.fill_input_form(text_to_copy)
    popup_iframe_page.submit_input_form()
    assert popup_iframe_page.get_result_text() == "Correct!"


@pytest.mark.positive
def test_cancel_iframe_popup(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_iframe_and_switch_to_it()
    popup_iframe_page.switch_to_main_window()
    popup_iframe_page.click_close_button()


@pytest.mark.negative
@pytest.mark.parametrize("invalid_data", ["  ", "hglhhkjnk", "*"])
def test_submit_input_form_with_invalid_data(popup_iframe_page, invalid_data):
    popup_iframe_page.open()
    popup_iframe_page.open_iframe_and_switch_to_it()
    popup_iframe_page.switch_to_main_window()
    popup_iframe_page.click_check_button()
    popup_iframe_page.fill_input_form(invalid_data)
    popup_iframe_page.submit_input_form()
    assert popup_iframe_page.get_result_text() == "Nope. Better luck next time!"




