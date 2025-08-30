def swap_first_and_last_elements(source_list: list) -> list:
    """
    The function can swap first and the last elements of the list

    Args:
        source_list: source list of elements

    Returns:
        swapped list
    """
    first = source_list[0]
    last = source_list[len(source_list)-1]
    source_list[0] = last
    source_list[len(source_list)-1] = first
    return source_list

print(swap_first_and_last_elements([1, 2, 3, 4]))