import pytest

input = [4, 1, 4, 2, 3]
# inputs = [[4, 1, 4, 2, 3],
#           [1, 1],
#           [2, 1, 4],
#           [3, -6, -5, -7],
#           [4, 1, 1, 3, 2],
#           [5, 1, 4, 2, -1, 6],
#           [6, 11, 7, 4, 2, 1, 6]]
output = "Jolly"
# outputs = ["Jolly",
#            "Jolly",
#            "Not jolly",
#            "Jolly",
#            "Not jolly",
#            "Not jolly",
#            "Jolly"]

"""
구현 방안
- 1부터 n-1까지 수가 담겨 있는 set 자료구조인 변수 set_input을 만든다.
- 문제에서 주어진 n개의 정수가 담겨 있는 배열을 반복문을 돌면서 차를 구한다. 
- 차를 set_input에서 pop한다.
    - 원소가 없어서 pop을 못하는 경우, 졸리점프가 아니므로 Not jolly를 출력한다.
"""


def test_simple():
    assert output == jolly_jumpers(input)


def jolly_jumpers(input):
    set_input = set(range(1, input[0]))
    try:
        remove_diff_from_set(set_input)
    except KeyError:
        return "Not jolly"
    return "Jolly"


def remove_diff_from_set(set_input):
    for index in range(1, len(input) - 1):
        diff = abs(input[index] - input[index + 1])
        set_input.remove(diff)


if __name__ == '__main__':
    question = [4, 1, 4, 2, 3]
    answer = jolly_jumpers(question)
    print(answer)
