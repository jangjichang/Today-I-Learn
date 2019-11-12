"""
Runtime: 56 ms, faster than 45.71% of Python online submissions for Find the Duplicate Number.
Memory Usage: 13.6 MB, less than 45.24% of Python online submissions for Find the Duplicate Number.
"""
# https://github.com/python/cpython/blob/master/Lib/collections/__init__.py#L542 건호 풀이 설명 추가

import pytest_watch

nums = [1, 3, 4, 2, 2]
output = 2


def test_simple():
    assert solution(nums) == output

def solution(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return nums[i]

if __name__ == "__main__":
    solution(nums)
