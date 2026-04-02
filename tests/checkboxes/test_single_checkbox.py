import pytest


@pytest.mark.positive
def test_default_elements_state(checkbox_single_page):
    checkbox_single_page.open()
    assert checkbox_single_page.count_checkboxes() == 1
    assert checkbox_single_page.get_checkbox_name() == "Select me or not"
    assert checkbox_single_page.get_button_name() == "Submit"
    assert checkbox_single_page.button_is_enabled()


@pytest.mark.positive
def test_checked_checkbox_shows_result_after_submit(checkbox_single_page) -> None:
    checkbox_single_page.open()
    checkbox_single_page.check_checkbox()
    assert checkbox_single_page.checkbox_is_checked()
    checkbox_single_page.submit_button()
    assert checkbox_single_page.get_result_text() == "select me or not"


@pytest.mark.negative
def test_unchecked_checkbox_not_show_result_after_submit(checkbox_single_page) -> None:
    checkbox_single_page.open()
    checkbox_single_page.submit_button()
    checkbox_single_page.result_is_not_present()

