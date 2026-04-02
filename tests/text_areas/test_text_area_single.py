import pytest


@pytest.mark.positive

def test_area_single_initial_state(text_area_single_page) -> None:
    text_area_single_page.open()
    assert text_area_single_page.get_text_area_name() == "Text area*"
    text_area_single_page.is_required_field()


@pytest.mark.positive
def test_submit_when_text_area_filled(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.clear_text_area()
    text_area_single_page.fill("Hello!")
    text_area_single_page.submit()
    assert text_area_single_page.get_result_text() == "Hello!"


@pytest.mark.negative
def test_submit_when_text_area_not_filled(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.clear_text_area()
    text_area_single_page.submit()
    assert text_area_single_page.get_validation_message() == "Please fill out this field."


@pytest.mark.negative
def test_submit_when_text_area_filled_with_only_spaces(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.clear_text_area()
    text_area_single_page.fill("  ")
    text_area_single_page.submit()
    assert text_area_single_page.get_error_message() == "This field is required."
