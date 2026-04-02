from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class DragAndDropImagePage(BasePage):
    URL = "https://www.qa-practice.com/elements/dragndrop/images"
    BOXES = { "top": (By.ID, "rect-droppable1"), "bottom" : (By.ID, "rect-droppable2")}
    IMAGE = (By.CSS_SELECTOR, "img[src='/static/home/smile.png']")


    def count_boxes(self):
        return len(self.browser.find_elements(By.CSS_SELECTOR, ".rect-droppable.ui-droppable"))

    def box_is_visible(self, box):
        return self.find(self.BOXES[box]).is_displayed()

    def img_is_visible(self):
        box =  self.find(self.BOXES["top"])
        return box.find_element(*self.IMAGE).is_displayed()


    def drag_image_to_box(self, droppable_box):
        actions = ActionChains(self.browser)
        img = self.find(self.IMAGE)
        box = self.find(self.BOXES[droppable_box])
        actions.drag_and_drop(img, box).perform()


    def get_text_in_droppable_box(self, droppable_box):
        return self.find(self.BOXES[droppable_box]).text

    def image_inside_box(self, box_name):
        box = self.find(self.BOXES[box_name])
        return len(box.find_elements(*self.IMAGE)) > 0

