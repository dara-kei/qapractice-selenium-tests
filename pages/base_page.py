from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    URL = None

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        if not self.URL:
            raise NotImplementedError("Page URL is not defined")
        self.browser.get(self.URL)


    def find(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

