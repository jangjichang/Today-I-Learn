import pytest

input = ['Tom', 'Jerry', 'Mike', 'Tom']
output = ['Tom']


def test_simple():
    assert output == duplicate_list(input)


def duplicate_list(input):
    if is_not_duplicate(input):
        return []

    return find_duplicate_element(input)


def is_not_duplicate(input):
    return len(input) == len(set(input))


def find_duplicate_element(input):
    counter_dict = dict()
    duplicate_list = list()
    for key in input:
        counter_dict = update_counter_dict(counter_dict, key)
        duplicate_list = update_duplicate_list(counter_dict, duplicate_list, key)
    return duplicate_list


def update_counter_dict(counter_dict, key):
    if not counter_dict.get(key):
        counter_dict[key] = 0
    counter_dict[key] += 1
    return counter_dict


def update_duplicate_list(counter_dict, duplicate_list, key):
    if counter_dict[key] >= 2 and key not in duplicate_list:
        duplicate_list.append(key)
    return duplicate_list


if __name__ == '__main__':
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    duplicate_list = find_duplicate_element(name)
    print(duplicate_list)
