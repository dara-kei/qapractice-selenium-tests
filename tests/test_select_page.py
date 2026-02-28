from pages.select_page import ProgrammingLanguage
import pytest

def test_select_field(select_page):
    select_page.open()
    assert select_page.select_is_named() == "Choose language*"
    assert select_page.select_is_required()


@pytest.mark.parametrize('option', [x.value for x in ProgrammingLanguage])
def test_result_should_be_displayed_after_selecting_option(select_page, option):
    select_page.open()
    select_page.choose_select_option(option)
    select_page.submit()
    assert select_page.get_result_text() == option


def test_form_should_not_submit_when_no_option_selected(select_page):
    select_page.open()
    select_page.submit()
    assert select_page.get_validation_message() == "Please select an item in the list."

