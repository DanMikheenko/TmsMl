def reverse_list(source_list: list) -> list:
    """
    The finction is the simplest way to reverse list of elements

    Args:
        source_list: source list of elements

    Returns:
        reversed list
    """
    source_list.reverse()
    return source_list

def reverse_list_more_complicated_way(source_list: list) -> list:
    """
    The finction can reverse list of elements

    Args:
        source_list: source list of elements

    Returns:
        reversed list
    """
    reversed_list = []
    for item in source_list:
        reversed_list.insert(0, item)
    return reversed_list

print(reverse_list([1, 2, 3, 4]))
print(reverse_list_more_complicated_way([1, 2, 3, 4]))