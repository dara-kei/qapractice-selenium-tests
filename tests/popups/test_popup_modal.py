import pytest


@pytest.mark.positive
def test_name_of_button_that_open_popup(popup_modal_page):
    popup_modal_page.open()
    assert popup_modal_page.get_button_name() == "Launch Pop-Up"


@pytest.mark.xfail(reason="Bug: wrong name for a button", strict=False)
@pytest.mark.positive
def test_popup_initial_state(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.click_button()
    assert popup_modal_page.popup_is_visible()
    assert popup_modal_page.get_popup_title() == "I am a Pop-Up"
    assert popup_modal_page.get_checkbox_text() == "Select me or not"
    assert popup_modal_page.get_number_of_buttons() == 2
    assert popup_modal_page.get_popup_buttons_names()[0] == "Send"
    assert popup_modal_page.get_popup_buttons_names()[1] == "Cancel"


@pytest.mark.positive
def test_send_popup_value_with_checkbox_checked(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.click_button()
    popup_modal_page.check_popup_checkbox()
    assert popup_modal_page.checkbox_is_checked()
    popup_modal_page.submit_popup()
    assert popup_modal_page.get_text_result() == "select me or not"


@pytest.mark.positive
def test_send_popup_value_with_checkbox_unchecked(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.click_button()
    assert not popup_modal_page.checkbox_is_checked()
    popup_modal_page.submit_popup()
    assert popup_modal_page.get_text_result() == "None"


@pytest.mark.positive
def test_cancel_popup(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.click_button()
    popup_modal_page.cancel_popup()
    assert not popup_modal_page.popup_is_visible()
