import pytest_watch

nums = [2, 2, 1]
output = 1


def test_simple():
    assert solution(nums) == output

def solution(nums):
    """
    O(n^2)
    """

    # answer = list()
    # for i in nums:
    #     if i in answer:
    #         answer.remove(i)
    #     else:
    #         answer.append(i)
    # return answer[0]


    """
    O(n)
    """
    answer = dict()
    for i in nums:
        try:
            answer.pop(i)
        except:
            answer[i] = 1
    return answer.popitem()[0]