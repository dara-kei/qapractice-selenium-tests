def test_button_exists(simple_button_page):

    simple_button_page.open()
    simple_button_page.button_should_be_displayed()


def test_button_name(simple_button_page):
    simple_button_page.open()
    simple_button_page.button_should_have_name("Click")


def test_click_button(simple_button_page):
    simple_button_page.open()
    simple_button_page.button().click()
    simple_button_page.result_should_have_text("Submitted")

