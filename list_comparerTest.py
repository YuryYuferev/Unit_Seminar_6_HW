import pytest

from list_comparer import ListComparer


@pytest.fixture
def list_comparer():
    return ListComparer()


def test_compare_lists_with_different_averages(list_comparer):
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    assert list_comparer.compare_lists(list1, list2) == "Второй список имеет большее среднее значение"


def test_compare_lists_with_different_averages2(list_comparer):
    list1 = [6, 7, 8, 9, 10]
    list2 = [1, 2, 3, 4, 5]
    assert list_comparer.compare_lists(list1, list2) == "Первый список имеет большее среднее значение"


def test_compare_lists_with_invalid_argument(list_comparer):
    with pytest.raises(TypeError):
        list_comparer.compare_lists(10, [1, 2, 3, 4, 5])


def test_compare_lists_with_equal_averages(list_comparer):
    list1 = [10, 10, 10, 9, 1]
    list2 = [6, 7, 8, 9, 10]
    assert list_comparer.compare_lists(list1, list2) == "Средние значения равны"



