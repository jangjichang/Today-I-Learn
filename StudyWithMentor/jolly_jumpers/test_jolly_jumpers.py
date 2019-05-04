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
