def test_buton_state(looks_like_button_page):
    looks_like_button_page.open()
    assert looks_like_button_page.button_is_displayed()
    assert looks_like_button_page.get_button_name() == "Click"


def test_looks_like_a_button_click_shows_confirmation(looks_like_button_page) -> None:
    looks_like_button_page.open()
    looks_like_button_page.submit_button()
    assert looks_like_button_page.get_result_text() == "Submitted"
