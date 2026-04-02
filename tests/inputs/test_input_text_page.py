import pytest


@pytest.mark.positive
def test_input_is_required(input_text_page):
    input_text_page.open()
    assert input_text_page.text_input_is_required_field()


@pytest.mark.positive
@pytest.mark.parametrize('text', ["hh", "Fgh77_-", "1234567890123456789012345"])
def test_valid_text_input_submission(input_text_page, text):
    input_text_page.open()
    input_text_page.clear_input()
    input_text_page.input_text(text)
    input_text_page.press_enter()
    assert input_text_page.get_text_result() == text


@pytest.mark.negative
def test_empty_text_input_shows_validation_error(input_text_page):
    input_text_page.open()
    input_text_page.clear_input()
    input_text_page.press_enter()
    assert input_text_page.get_validation_message() == "Please fill out this field."

@pytest.mark.negative
def test_whitespace_only_input_shows_validation_error(input_text_page):
    input_text_page.open()
    input_text_page.clear_input()
    input_text_page.input_text("  ")
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.get_error_message() == "This field is required."


@pytest.mark.negative
@pytest.mark.parametrize("invalid_data, error_message",
                         [("j", "Please enter 2 or more characters"),
                          ("12345678901234567890123456", "Please enter no more than 25 characters"),
                          ("Привет", "Enter a valid string consisting of letters, numbers, underscores or hyphens."),
                          ("@@", "Enter a valid string consisting of letters, numbers, underscores or hyphens.")],
                         ids=["less_letters",
                              "more_letter",
                              "non_latin_letters",
                              "invalid_symbols"]
                         )
def test_invalid_data_input_shows_validation_error(input_text_page, invalid_data, error_message):
    input_text_page.open()
    input_text_page.clear_input()
    input_text_page.input_text(invalid_data)
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.get_error_message() == error_message