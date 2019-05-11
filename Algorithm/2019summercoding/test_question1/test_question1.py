"""
풀이법:

"""
from collections import Counter
import pytest


def test_simple():
    assert 4 == solution([1, 2, 4, 3, 3])
    assert 5 == solution([2, 3, 4, 4, 2, 1, 3, 1])
    assert 2 == solution([2, 2, 2, 2])
    assert 3 == solution([1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert 3 == solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert 4 == solution([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert 4 == solution([4, 4, 4, 4])
    assert 4 == solution([4, 4, 4, 3])
    assert 4 == solution([4, 4, 4, 2])
    assert 4 == solution([4, 4, 4, 1])
    assert 1 == solution([1])
    assert 1 == solution([2])
    assert 1 == solution([3])
    assert 1 == solution([4])
    assert 3 == solution([4, 3, 2, 1])


def solution(s):
    answer = 0
    temp = 0
    c = Counter(s)
    if c.get(4):
        answer += c[4]
    if c.get(3):
        answer += c[3]
        if c.get(1):
            c[1] -= c[3]
    if c.get(2) or c.get(1):
        temp += c[2] * 2
        if c.get(1):
            if c[1] >= 0:
                temp += c[1]
        answer = answer + (temp // 4)
        if temp % 4 != 0:
            answer += 1
    return answer



    # for key, value in reversed(sorted(c.items())):
    #     if key == 4:
    #         answer += c[key]
    #     elif key == 3:
    #         answer += c[key]
    #         if c.get(1):
    #             c[1] -= c[key]
    #     elif key == 2 or key == 1:
    #         temp = 0
    #         if c.get(2):
    #             temp += c[2] * 2
    #         if c.get(1):
    #             if c[1] >= 0:
    #                 temp += c[1]
    #         answer = answer + (temp // 4)
    #         if temp % 4 != 0:
    #             answer += 1
    #         return answer
    #     else:
    #         return answer
    # return answer


if __name__ == '__main__':
    solution([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
