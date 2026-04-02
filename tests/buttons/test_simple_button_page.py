def test_button_state(simple_button_page):
    simple_button_page.open()
    assert simple_button_page.button_is_displayed()
    assert simple_button_page.get_button_name() == "Click"

def test_click_button(simple_button_page):
    simple_button_page.open()
    simple_button_page.submit_button()
    assert simple_button_page.get_result_text() == "Submitted"

