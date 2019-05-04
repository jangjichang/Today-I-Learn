import pytest_watch

input = [4, 1, 4, 2, 3]
# input = [5, 1, 4, 2, -1, 6]
output = "Jolly"
# output = "Not jolly"

"""
n개의 정수가 담겨 있는 배열을 반복문을 돌면서 차를 구한다. 
구한 차를 1부터 n-1까지의 수가 담겨 있는 set에서 pop한다.
    원소가 없어서 pop을 못하는 경우, 졸리점프가 아니므로 Not jolly를 출력한다. 
"""


def test_simple():
    assert output == jolly_jumpers(input)


def jolly_jumpers(input):
    set_input = set(range(1, input[0]))
    try:
        remove_from_set(set_input)
    except KeyError:
        return "Not jolly"
    return "Jolly"


def remove_from_set(set_input):
    for index in range(1, len(input) - 1):
        diff = abs(input[index] - input[index + 1])
        set_input.remove(diff)
