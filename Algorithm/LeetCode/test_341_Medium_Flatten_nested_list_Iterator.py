import pytest_watch

input = [1,[4,[6]]]
answer = []
output = [1, 4, 6]


def test_simple():
    assert solution(input, answer) == output

"""
i가 int이면 반환
i가 list이면 
"""
def solution(input, answer):
    for i in input:
        if isinstance(i, int):
            answer.append(i)
        else:
            solution(i, answer)
            input.pop()
    return answer


if __name__ == "__main__":
    # a = [1, 2, 3,]
    # for i in a:
    #     print(isinstance(i, int))
    output = solution(input, answer)
    print(output)