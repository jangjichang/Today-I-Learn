import pytest
input = ['Tom', 'Jerry', 'Mike', 'Tom']
output = ['Tom']


def test_simple():
    assert output == duplicate_list(input)


def duplicate_list(input):
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
    input_dict = dict()
    result = list()

    for i in input:
        add_to_dict(input_dict, result, i)


def add_to_dict(input, result, x):
    if not input.get(x):
       input[x] = 0
    input[x] += 1
    if input.counter(x) >= 2 and x not in result:
        result.append(x)


if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    result = duplicate_list(name)
    print(result)
