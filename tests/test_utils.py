from app.utils import get_next_page, get_page_count, get_prev_page


def test_get_page_count():
    assert get_page_count(0, 10) == 0
    assert get_page_count(10, 10) == 1
    assert get_page_count(11, 10) == 1
    assert get_page_count(20, 10) == 2
    assert get_page_count(21, 10) == 2
    assert get_page_count(30, 10) == 3


def test_get_prev_page():
    assert get_prev_page(0) is None
    assert get_prev_page(1) == 0
    assert get_prev_page(2) == 1
    assert get_prev_page(3) == 2


def test_get_next_page():
    assert get_next_page(0, 0, 10) is None
    assert get_next_page(10, 0, 10) == 1
    assert get_next_page(11, 0, 10) == 1
    assert get_next_page(20, 0, 10) == 1
    assert get_next_page(21, 0, 10) == 1
    assert get_next_page(30, 0, 10) == 1
    assert get_next_page(30, 1, 10) == 2
    assert get_next_page(30, 2, 10) == 3
    assert get_next_page(30, 3, 10) is None
