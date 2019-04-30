import pytest
input = ['Tom', 'Jerry', 'Mike', 'Tom']
output = ['Tom']


def test_simple():
    assert output == duplicate_check(input)


def duplicate_check(input):
    if is_not_duplicate(input):
        return []

    return(find_duplicate_element(input))


def is_not_duplicate(input):
    return len(input) == len(set(input))


def find_duplicate_element(input):
    result = []
    for i in set(input):
        if input.count(i) >= 2:
            result.append(i)
    return result
