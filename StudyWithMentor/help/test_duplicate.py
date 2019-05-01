import pytest
input = ['Tom', 'Jerry', 'Mike', 'Tom']
output = ['Tom']


def test_simple():
    assert output == duplicate_check(input)


def duplicate_check(input):
    """
    Return duplicate str
    :param input: string list
    :return: redundant list of elements
    """
    if is_not_duplicate(input):
        return []

    return find_duplicate_element(input)


def is_not_duplicate(input):
    return len(input) == len(set(input))


def find_duplicate_element(input):
    return [x for x in set(input) if input.count(x) >= 2]


if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    result = duplicate_check(name)
    print(result)
