def test_button_visibility(alert_prompt_page):
    alert_prompt_page.open()
    alert_prompt_page.button_is_visible()


def test_alert_accept(alert_prompt_page):
    alert_prompt_page.open()
    alert_prompt_page.click_button()
    assert alert_prompt_page.get_alert_text() == "Please enter some text"
    alert_prompt_page.fill_text("Hello")
    alert_prompt_page.alert_accept()
    assert alert_prompt_page.get_result_text() == "Hello"


def test_alert_cancel(alert_prompt_page):
    alert_prompt_page.open()
    alert_prompt_page.click_button()
    alert_prompt_page.alert_cancel()
    assert alert_prompt_page.get_result_text() == "You canceled the prompt"
