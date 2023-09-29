def get_page_count(item_count: int, page_size: int):
    return round(item_count / page_size)


def get_prev_page(page_number: int):  # noqa: E501
    return page_number - 1 if page_number > 0 else None


def get_next_page(item_count: int, page_number: int, page_size: int):
    page_count = get_page_count(item_count, page_size)
    if page_number >= page_count:
        return None

    return page_number + 1
