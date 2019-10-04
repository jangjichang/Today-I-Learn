import pytest


def test_simple():
    assert 3 == solution([1, 3, 2, 5, 4], 9)
    assert 4 == solution([2, 2, 3, 3], 10)


def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            return answer
    return answer