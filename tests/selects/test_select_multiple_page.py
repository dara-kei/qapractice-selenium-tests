import pytest
from data.travel_options import Places, Transport, Date


@pytest.mark.positive
def test_loading_page(select_multiple_page):
    select_multiple_page.open()
    assert select_multiple_page.count_selects() == 3
    assert select_multiple_page.get_first_select_name() == "Choose the place you want to go*"
    assert select_multiple_page.get_second_select_name() == "Choose how you want to get there*"
    assert select_multiple_page.get_third_select_name() == "Choose when you want to go*"
    assert select_multiple_page.first_select_is_required()
    assert select_multiple_page.second_select_is_required()
    assert select_multiple_page.third_select_is_required()


# # в этом тесте будут перебираться все комбинации (60 тестов!), что избыточно, хотя в данном тесте меньше по коду
# @pytest.mark.parametrize("first_select, first_select_options", [("first", x.value) for x in Places])
# @pytest.mark.parametrize("second_select, second_select_options", [("second",x.value) for x in Transport])
# @pytest.mark.parametrize("third_select, third_select_options", [("third",x.value) for x in Date])
# def test_form_should_submit_when_all_required_selects_are_selected(select_multiple_page,
#                                                                    first_select, first_select_options,
#                                                                    second_select, second_select_options,
#                                                                    third_select, third_select_options):
#     select_multiple_page.open()
#     select_multiple_page.choose_select_option(first_select, first_select_options)
#     select_multiple_page.choose_select_option(second_select, second_select_options)
#     select_multiple_page.choose_select_option(third_select, third_select_options)
#     select_multiple_page.submit()
#     assert select_multiple_page.get_result_text() == f"to go by {second_select_options.lower()} to the {first_select_options.lower()} {third_select_options.lower()}"


# проверка всех вариантов Places
@pytest.mark.positive
@pytest.mark.parametrize("select_option", [x.value for x in Places])
def test_submit_with_all_first_select_options(select_multiple_page, select_option):
    select_multiple_page.open()
    select_multiple_page.choose_select_option("first", select_option)
    select_multiple_page.choose_select_option("second", "Car")
    select_multiple_page.choose_select_option("third", "Today")
    select_multiple_page.submit()
    assert select_multiple_page.get_result_text() == f"to go by car to the {select_option.lower()} today"


#  проверка всех вариантов Transport
@pytest.mark.positive
@pytest.mark.parametrize("select_option", [x.value for x in Transport])
def test_submit_with_all_second_select_options(select_multiple_page, select_option):
    select_multiple_page.open()
    select_multiple_page.choose_select_option("first", "Mountains")
    select_multiple_page.choose_select_option("second", select_option)
    select_multiple_page.choose_select_option("third", "Tomorrow")
    select_multiple_page.submit()
    assert select_multiple_page.get_result_text() == f"to go by {select_option.lower()} to the mountains tomorrow"


#  проверка оставшегося варианта Data
@pytest.mark.positive
@pytest.mark.parametrize("select_option", [x.value for x in Transport])
def test_submit_with_last_option_of_third_select(select_multiple_page, select_option):
    select_multiple_page.open()
    select_multiple_page.choose_select_option("first", "Old town")
    select_multiple_page.choose_select_option("second", "Train")
    select_multiple_page.choose_select_option("third", "Next week")
    select_multiple_page.submit()
    assert select_multiple_page.get_result_text() == f"to go by train to the old town next week"


@pytest.mark.negative
def test_not_submission_when_no_option_selected(select_multiple_page):
    select_multiple_page.open()
    select_multiple_page.submit()
    assert select_multiple_page.get_validation_message("first") == "Please select an item in the list."


@pytest.mark.negative
@pytest.mark.parametrize("selected_select_1, option1, selected_select_2, option2, unselected_select",
    [
        ("second", "Car", "third", "Today", "first"),
        ("first", "Sea", "third", "Today", "second"),
        ("first", "Sea", "second", "Car", "third"),
    ]
)
def test_not_submission_with_one_select_not_selected(select_multiple_page, selected_select_1, option1, selected_select_2, option2, unselected_select):
    select_multiple_page.open()
    select_multiple_page.choose_select_option(selected_select_1, option1)
    select_multiple_page.choose_select_option(selected_select_2, option2)
    select_multiple_page.submit()
    assert select_multiple_page.get_validation_message(unselected_select) == "Please select an item in the list."