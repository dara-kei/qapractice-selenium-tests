import pytest


@pytest.mark.positive
def test_checkboxes_page_initial_state(checkboxes_page):
    checkboxes_page.open()
    assert checkboxes_page.count_checkboxes() == 3
    assert checkboxes_page.get_first_checkbox_name() == "One"
    assert checkboxes_page.get_second_checkbox_name() == "Two"
    assert checkboxes_page.get_third_checkbox_name() == "Three"
    assert checkboxes_page.get_button_name() == "Submit"
    assert checkboxes_page.button_is_enabled()


@pytest.mark.positive
@pytest.mark.parametrize("checkbox, expected_result", [("One", "one"),
                                                       ("Two", "two"),
                                                       ("Three", "three")])
def test_one_checked_checkbox_shows_result(checkboxes_page, checkbox, expected_result):
    checkboxes_page.open()
    assert checkboxes_page.checkbox_is_visible(checkbox)
    checkboxes_page.check_checkbox(checkbox)
    assert checkboxes_page.checkbox_is_checked(checkbox)
    checkboxes_page.submit_button()
    assert checkboxes_page.get_result_text() == expected_result


@pytest.mark.positive
@pytest.mark.parametrize("first_checkbox, second_checkbox, expected_result",
                         [("One", "Two", "one, two"),
                          ("Two", "Three", "two, three"),
                          ("One","Three", "one, three")])
def test_two_checked_checkboxes_shows_result(checkboxes_page, first_checkbox, second_checkbox, expected_result):
    checkboxes_page.open()
    checkboxes_page.check_checkbox(first_checkbox)
    checkboxes_page.check_checkbox(second_checkbox)
    checkboxes_page.submit_button()
    assert checkboxes_page.get_result_text() == expected_result


@pytest.mark.positive
def test_all_checked_checkboxes_shows_result(checkboxes_page):
    checkboxes_page.open()
    checkboxes_page.check_checkbox("One")
    checkboxes_page.check_checkbox("Two")
    checkboxes_page.check_checkbox("Three")
    checkboxes_page.submit_button()
    assert checkboxes_page.get_result_text() == "one, two, three"



@pytest.mark.negative
def test_not_checked_checkboxes_not_show_result(checkboxes_page):
    checkboxes_page.open()
    checkboxes_page.submit_button()
    checkboxes_page.result_is_not_present()