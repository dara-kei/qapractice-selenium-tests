import pytest


@pytest.mark.positive
def test_new_tab_link_should_open_new_page(new_tab_with_button_page) -> None:
    new_tab_with_button_page.open()
    assert new_tab_with_button_page.number_of_windows() == 1
    new_tab_with_button_page.open_new_page()
    assert new_tab_with_button_page.get_page_url() == new_tab_with_button_page.NEW_URL
    assert new_tab_with_button_page.result_text_of_new_page() == "I am a new page in a new tab"
    new_tab_with_button_page.close_new_page()




