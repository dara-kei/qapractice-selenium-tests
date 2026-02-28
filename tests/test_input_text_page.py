import pytest

@pytest.mark.parametrize('text', ["hh", "Fgh77_-", "1234567890123456789012345"])
def test_right_input(input_text_page, text):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.input_text_in_field(text)
    input_text_page.press_enter()
    assert input_text_page.result.text == text

def test_empty_input(input_text_page):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.press_enter()
    assert input_text_page.get_validation_message() == "Please fill out this field."


def test_input_with_less_letters(input_text_page):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.input_text_in_field("h")
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.error_message.text == "Please enter 2 or more characters"


def test_input_with_more_letters(input_text_page):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.input_text_in_field("12345678901234567890123456")
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.error_message.text == "Please enter no more than 25 characters"


@pytest.mark.parametrize("text", ["привет", "@@"])
def test_input_with_non_latin_characters(input_text_page, text):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.input_text_in_field(text)
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.error_message.text == "Enter a valid string consisting of letters, numbers, underscores or hyphens."


def test_input_with_space(input_text_page):
    input_text_page.open()
    input_text_page.clear_field()
    input_text_page.input_text_in_field("  ")
    input_text_page.press_enter()
    assert input_text_page.error_message_is_visible()
    assert input_text_page.error_message.text == "This field is required."

