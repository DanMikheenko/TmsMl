def get_three_most_often_chars_in_string(source_string: str) -> list:
    chars_dictionary : dict = {}
    for char in source_string:
        if char == " ":
            continue
        if char in chars_dictionary:
            chars_dictionary[char] += 1
        else:
            chars_dictionary[char] = 1
    sorted_chars = sorted(chars_dictionary.items(), key=lambda item: item[1], reverse=True)
    three_most_often_chars = [char[0] for char in sorted_chars[:3]]
    return three_most_often_chars 

print(get_three_most_often_chars_in_string("abcbcay   yyyy"))