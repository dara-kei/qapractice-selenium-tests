import pytest


def test_checkboxes_page_initial_state(checkboxes_page):
    checkboxes_page.open()
    assert checkboxes_page.count_checkboxes() == 3
    assert checkboxes_page.get_first_checkbox_name() == "One"
    assert checkboxes_page.get_second_checkbox_name() == "Two"
    assert checkboxes_page.get_third_checkbox_name() == "Three"
    assert checkboxes_page.get_button_name() == "Submit"
    assert checkboxes_page.button_is_enabled()


def test_checkboxes_not_checked(checkboxes_page):
    checkboxes_page.open()
    checkboxes_page.submit_button()
    assert checkboxes_page.result_is_not_present()



@pytest.mark.parametrize("checkbox, expected_result", [("one", "one"),
                                                       ("two", "two"),
                                                       ("three", "three")])
def test_checkboxes(checkboxes_page, checkbox, expected_result):
    checkboxes_page.open()
    assert checkboxes_page.checkbox_is_visible(checkbox)
    checkboxes_page.check_checkbox(checkbox)
    assert checkboxes_page.checkbox_is_checked(checkbox)
    checkboxes_page.submit_button()
    assert checkboxes_page.result() == expected_result

@pytest.mark.parametrize("first_checkbox, second_checkbox, expected_result",
                         [("one", "two", "one, two"),
                          ("two", "three", "two, three"),
                          ("one","three", "one, three")])
def test_two_checkboxes_checked(checkboxes_page, first_checkbox, second_checkbox, expected_result):
    checkboxes_page.open()
    checkboxes_page.check_checkbox(first_checkbox)
    checkboxes_page.check_checkbox(second_checkbox)
    checkboxes_page.submit_button()
    assert checkboxes_page.result() == expected_result


def test_all_checkboxes_checked(checkboxes_page):
    checkboxes_page.open()
    checkboxes_page.check_checkbox("one")
    checkboxes_page.check_checkbox("two")
    checkboxes_page.check_checkbox("three")
    checkboxes_page.submit_button()
    assert checkboxes_page.result() == "one, two, three"
