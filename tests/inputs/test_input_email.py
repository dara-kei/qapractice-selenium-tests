import pytest


@pytest.mark.positive
def test_input_is_required(input_email_page):
    input_email_page.open()
    assert input_email_page.text_input_is_required_field()


@pytest.mark.positive
@pytest.mark.parametrize('valid_email', ["user@google.com", "user@localhost"])
def test_valid_email_input_submission(input_email_page, valid_email)-> None:
    input_email_page.open()
    input_email_page.clear_input()
    input_email_page.input_text(valid_email)
    input_email_page.press_enter()
    assert input_email_page.get_text_result() == valid_email

@pytest.mark.negative
def test_empty_email_input_shows_error_message(input_email_page)-> None:
    input_email_page.open()
    input_email_page.clear_input()
    input_email_page.input_text("")
    input_email_page.press_enter()
    assert input_email_page.get_validation_message() == "Please fill out this field."


@pytest.mark.negative
def test_whitespace_only_email_input_shows_error_message(input_email_page)-> None:
    input_email_page.open()
    input_email_page.clear_input()
    input_email_page.input_text(" ")
    input_email_page.press_enter()
    assert input_email_page.get_error_message() == "This field is required."


@pytest.mark.negative
@pytest.mark.parametrize("invalid_email", ["userlocalhost", "юсер@localhost"])
def test_invalid_characters_email_input_shows_validation_error(input_email_page,invalid_email)-> None:
    input_email_page.open()
    input_email_page.clear_input()
    input_email_page.input_text(invalid_email)
    input_email_page.press_enter()
    assert input_email_page.get_error_message() == "Enter a valid email address."
