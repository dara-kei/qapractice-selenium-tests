def test_button_visibility(alert_confirm_page):
    alert_confirm_page.open()
    alert_confirm_page.button_is_visible()


def test_alert_accept(alert_confirm_page):
    alert_confirm_page.open()
    alert_confirm_page.click_button()
    assert alert_confirm_page.get_alert_text() == "Select Ok or Cancel"
    alert_confirm_page.alert_accept()
    assert alert_confirm_page.get_result_text() == "Ok"

def test_alert_cancel(alert_confirm_page):
    alert_confirm_page.open()
    alert_confirm_page.click_button()
    alert_confirm_page.alert_cancel()
    assert alert_confirm_page.get_result_text() == "Cancel"

