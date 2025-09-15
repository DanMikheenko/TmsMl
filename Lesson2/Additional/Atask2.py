def is_substr_in_string(substring: str, string: str) -> str:
    substring = substring.lower()
    string = string.lower()
    if substring in string:
        return "Есть контакт!"
    else:
        return "Мимо!"

print(is_substr_in_string("М12", "м123"))