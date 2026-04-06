from pages.new_tabs.base_new_tabs_page import BaseNewTabPage
from selenium.webdriver.common.by import By


class NewTabWithButtonPage(BaseNewTabPage):
    URL = "https://www.qa-practice.com/elements/new_tab/button"
    NEW_URL = "https://www.qa-practice.com/elements/new_tab/new_page"
    NEW_TAB = (By.ID, "new-page-button")
