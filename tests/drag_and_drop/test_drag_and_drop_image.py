
import pytest


@pytest.mark.positive
# @pytest.mark.xfail(reason="Bug: img is in wrong square", strict=False)
def test_drag_and_drop_image_page_initial_state(drag_and_drop_image_page):
    drag_and_drop_image_page.open()
    assert drag_and_drop_image_page.count_boxes() == 2
    assert drag_and_drop_image_page.box_is_visible("top")
    assert drag_and_drop_image_page.box_is_visible("bottom")
    assert drag_and_drop_image_page.img_is_visible()


@pytest.mark.positive
def test_drag_and_drop_image_between_boxes(drag_and_drop_image_page):
    drag_and_drop_image_page.open()
    for _ in range(3):
        drag_and_drop_image_page.drag_image_to_box("bottom")
        assert drag_and_drop_image_page.get_text_in_droppable_box("bottom") == "Dropped!"
        assert drag_and_drop_image_page.image_inside_box("bottom")
        assert not drag_and_drop_image_page.image_inside_box("top")
        drag_and_drop_image_page.drag_image_to_box("top")
        assert drag_and_drop_image_page.get_text_in_droppable_box("top") == "Dropped!"
        assert drag_and_drop_image_page.image_inside_box("top")
        assert not drag_and_drop_image_page.image_inside_box("bottom")

