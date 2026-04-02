import pytest


@pytest.mark.positive
def test_drag_and_drop_page_initial_state(drag_and_drop_boxes_page):
    drag_and_drop_boxes_page.open()
    drag_and_drop_boxes_page.box_is_visible("botton")
    drag_and_drop_boxes_page.box_is_visible("top")


@pytest.mark.positive
def test_dragging_bottom_box_to_top_one(drag_and_drop_boxes_page):
    drag_and_drop_boxes_page.open()
    drag_and_drop_boxes_page.drag_box_to_target()
    assert drag_and_drop_boxes_page.get_text_in_top_box() == "Dropped!"
    assert drag_and_drop_boxes_page.draggable_text_should_be_inside_droppable() == "Dropped!\nDrag me"
