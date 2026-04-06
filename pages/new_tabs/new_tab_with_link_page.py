from pages.new_tabs.base_new_tabs_page import BaseNewTabPage
from selenium.webdriver.common.by import By


class NewTabLinkPage(BaseNewTabPage):
    URL = "https://www.qa-practice.com/elements/new_tab/link"
    NEW_URL = "https://www.qa-practice.com/elements/new_tab/new_page"
    NEW_TAB = (By.ID, "new-page-link")

