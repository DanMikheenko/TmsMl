def get_max_and_devide_by_list_length(source_list: list) -> float:
    """
    The function can find the maximum element of the list and divide the max by the length of the list

    Args:
        source_list: source list of elements

    Returns:
        modified list
    """
    max_element = max(source_list)
    list_length = len(source_list)
    return max_element / list_length

print(get_max_and_devide_by_list_length([1, 2, 3, 4, 12]))