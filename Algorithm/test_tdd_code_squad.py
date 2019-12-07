import re


def split_and_sum_integer(string):
    """자바지기님의 강의 `내가 TDD에 집착하는 이유는?`을 보고 작성한 예제

    Arguments:
        string {str} -- [숫자와 구분자가 포함된 문자열]

    Returns:
        [int]] -- [문자열에서 숫자의 합]
    """
    return sum([int(i) for i in re.findall('[0-9]+', string)])


def test_split_and_sum_integer():
    assert split_and_sum_integer("1,2,3") == 6
    assert split_and_sum_integer("1,2:3") == 6
    assert split_and_sum_integer("1,2") == 3
    assert split_and_sum_integer("1:2,3") == 6
    assert split_and_sum_integer("4,3,2:1") == 10
    assert split_and_sum_integer("10,9,8") == 27
