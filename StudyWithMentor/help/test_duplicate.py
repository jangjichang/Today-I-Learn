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
    counter_dict = dict()
    duplicate_list = list()
    for key in input:
        counter_dict = update_counter_dict(counter_dict, key)
        duplicate_list = update_duplicate_list(counter_dict, duplicate_list, key)
    return duplicate_list


def update_counter_dict(counter_dict, key):
    """
    :param counter_dict: 사전 자료 구조의 파라미터, key- 단어, value- 단어 빈도수
    :param key: list 반복인 원소 중 하나
    :return: 단어의 빈도수를 담고 있는 사전 자료 구조 변수, dict
    """
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
