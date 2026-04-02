
def test_button_visibility(alert_box_page):
    alert_box_page.open()
    assert alert_box_page.button_is_visible()


def test_alert_work(alert_box_page):
    alert_box_page.open()
    alert_box_page.click_button()
    assert alert_box_page.get_alert_text() == "I am an alert!"
    alert_box_page.alert_accept()
