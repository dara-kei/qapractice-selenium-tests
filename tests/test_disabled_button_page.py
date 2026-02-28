def test_initial_state_of_elements(disabled_button_page):
    disabled_button_page.open()
    disabled_button_page.drop_down_should_have_text("Disabled")
    disabled_button_page.button_should_be_disabled()
    disabled_button_page.button_should_have_name("Submit")


def test_button(disabled_button_page):
    disabled_button_page.open()
    disabled_button_page.choose_select_option("Enabled")
    disabled_button_page.drop_down_should_have_text("Enabled")
    disabled_button_page.choose_select_option("Disabled")
    disabled_button_page.drop_down_should_have_text("Disabled")
    disabled_button_page.choose_select_option("Enabled")
    disabled_button_page.submit_button()
    disabled_button_page.result_should_have_text("Submitted")

