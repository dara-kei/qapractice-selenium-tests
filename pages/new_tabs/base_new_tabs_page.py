from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseNewTabPage(BasePage):
    NEW_TAB = None
    RESULT = (By.ID, "result-text")

    def __init__(self, browser):
        super().__init__(browser)
        self.original_window = None


    def number_of_windows(self):
        return len(self.browser.window_handles)


    def open_new_page(self):
        # Store the ID of the original window
        self.original_window = self.browser.current_window_handle

        # Click the link which opens in a new window
        self.find(self.NEW_TAB).click()
        # Wait for the new window or tab
        WebDriverWait(self.browser, timeout = 10).until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.browser.window_handles:
            if window_handle != self.original_window:
                self.browser.switch_to.window(window_handle)
                break

        # Wait for the new tab to finish loading content
        WebDriverWait(self.browser, timeout = 10).until(EC.presence_of_element_located(self.RESULT))


    def get_page_url(self):
        return self.browser.current_url


    def result_text_of_new_page(self):
        return self.find(self.RESULT).text


    def close_new_page(self):
        self.browser.close()
        self.browser.switch_to.window(self.original_window)
