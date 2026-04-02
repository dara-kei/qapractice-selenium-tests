from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDropBoxesPage(BasePage):
    URL = "https://www.qa-practice.com/elements/dragndrop/boxes"
    BOXES = {"top" : (By.ID, "rect-droppable"), "botton" : (By.ID, "rect-draggable")}
    TEXT = (By.ID, "text-droppable")


    def box_is_visible(self, box):
        return self.find(self.BOXES[box]).is_displayed()


    def drag_box_to_target(self):
        actions = ActionChains(self.browser)
        actions.drag_and_drop(self.find(self.BOXES["botton"]), self.find(self.BOXES["top"])).perform()


    def get_text_in_top_box(self):
        return self.find(self.TEXT).text


    def draggable_text_should_be_inside_droppable(self):
        return self.find(self.BOXES["top"]).text