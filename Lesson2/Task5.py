def get_all_strings_from_list_equels_by_length(source_list: list) -> list:
    """
    The function finds the longest string in the list, adds "_" to the ending of all other strings
    to make their lengths equal to the length of the longest string and returns a list of modified strings.

    Args:
        source_list: source list of elements
    
    Returns:
        list of modified strings
    """
    max_length_of_the_string = 0
    for element in source_list:
        if isinstance(element, str) and len(element) > max_length_of_the_string:
            max_length_of_the_string = len(element)

    result = []
    for element in source_list:
        if isinstance(element, str):
            diff = max_length_of_the_string - len(element)
            result.append(element + "_" * diff)
    return result

print(get_all_strings_from_list_equels_by_length(["qwe", "qwerty", "q", "qw", "qwert"]))