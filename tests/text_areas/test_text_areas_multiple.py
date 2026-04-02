import pytest



@pytest.mark.positive
def test_areas_multiple_initial_state(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    assert text_areas_multiple_page.count_text_areas() == 3
    assert text_areas_multiple_page.get_first_text_area_name() == "First chapter*"
    assert text_areas_multiple_page.get_second_text_area_name() == "Second chapter"
    assert text_areas_multiple_page.get_third_text_area_name() == "Third chapter"
    assert text_areas_multiple_page.first_area_is_required()


@pytest.mark.positive
def test_submit_when_first_area_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first="Hello!")
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_result_text() == "Hello!"

@pytest.mark.positive
@pytest.mark.parametrize("second, third", [("World", None), (None, "World")])
def test_submit_when_two_areas_filled(text_areas_multiple_page, second, third) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first="Hello", second = second, third = third)
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_result_text() == "Hello\nWorld"


@pytest.mark.positive
def test_submit_when_all_areas_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first="Hello,", second = "my", third = "World!")
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_result_text() == 'Hello,\nMy\nWorld!'


@pytest.mark.negative
def test_submit_when_all_areas_empty(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.clear_text_area(0)
    text_areas_multiple_page.clear_text_area(1)
    text_areas_multiple_page.clear_text_area(2)
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_validation_message(0) == "Please fill out this field."


@pytest.mark.negative
def test_submit_when_required_area_not_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(second = "my", third = "World")
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_validation_message(0) == "Please fill out this field."



@pytest.mark.negative
def test_submit_when_first_text_area_filled_with_only_spaces(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first="  ")
    text_areas_multiple_page.hover_over_the_button()
    text_areas_multiple_page.submit()
    assert text_areas_multiple_page.get_error_message() == "This field is required."