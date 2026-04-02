def test_initial_state_of_elements(disabled_button_page):
    disabled_button_page.open()
    assert disabled_button_page.get_drop_down_text() == "Disabled"
    assert not disabled_button_page.button_is_enabled()
    assert disabled_button_page.get_button_name() == "Submit"


def test_button_state_can_be_changed_via_dropdown(disabled_button_page):
    disabled_button_page.open()
    disabled_button_page.choose_select_option("Enabled")
    assert disabled_button_page.get_drop_down_text() == "Enabled"
    assert disabled_button_page.button_is_enabled()
    disabled_button_page.choose_select_option("Disabled")
    assert disabled_button_page.get_drop_down_text() == "Disabled"
    assert not disabled_button_page.button_is_enabled()


def test_button_click_shows_confirmation(disabled_button_page):
    disabled_button_page.open()
    disabled_button_page.choose_select_option("Enabled")
    disabled_button_page.submit_button()
    assert disabled_button_page.get_result_text() == "Submitted"

