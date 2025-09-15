from collections import Counter

def count_it(source_string: str) -> dict:
    source_int_numbers = [int(ch) for ch in source_string]
    counter = Counter(source_int_numbers)
    most_three_numbers = dict(counter.most_common(3))
    
    return most_three_numbers


my_string = "00000111"
print(count_it(my_string))
