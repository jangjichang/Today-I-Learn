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
        if i in input_dict:
            input_dict[i] += 1
            if input_dict[i] >= 2:
                if not i in result:
                    result.append(i)
        else:
            input_dict[i] = 1
    return result


if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    result = duplicate_list(name)
    print(result)
