import pytest


@pytest.mark.positive
@pytest.mark.parametrize("valid_passwd", ["Tested1#", "Tested1#привет", "&&&&!%$@Tested66789"])
def test_valid_passwd_input_submission(input_password_page,valid_passwd)-> None:
    input_password_page.open()
    input_password_page.clear_input()
    input_password_page.input_text(valid_passwd)
    input_password_page.press_enter()
    assert input_password_page.get_text_result() == valid_passwd


@pytest.mark.negative
def test_empty_text_input_shows_validation_error(input_password_page)-> None:
    input_password_page.open()
    input_password_page.clear_input()
    input_password_page.input_text("")
    input_password_page.press_enter()
    assert input_password_page.get_validation_message() == "Please fill out this field."

@pytest.mark.negative
def test_whitespace_only_input_shows_validation_error(input_password_page)-> None:
    input_password_page.open()
    input_password_page.clear_input()
    input_password_page.input_text(" ")
    input_password_page.press_enter()
    assert input_password_page.get_error_message() == "This field is required."


@pytest.mark.negative
@pytest.mark.parametrize("invalid_passwd", ["tested1#", "Tested11", "Tested##", "Test1#"],
                         ids = ["passwd_without_one_uppercase_let",
                                "passwd_without_special_symbol",
                                "passwd_without_numbers",
                                "passwd_shorter_than_min_length"])
def test_invalid_passwd_input_shows_error_message(input_password_page, invalid_passwd)-> None:
    input_password_page.open()
    input_password_page.clear_input()
    input_password_page.input_text(invalid_passwd)
    input_password_page.press_enter()
    assert input_password_page.get_error_message() == "Low password complexity"

