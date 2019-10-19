import pytest_watch

nums = [2, 7, 11, 15]
target = 9
output = [0, 1]

def test_simple():
    assert solution(nums, target) == output

def solution(nums, target):
    """
    시간 복잡도: O(n^2)
    """
    for idx, value in enumerate(nums):
        for nextidx, nextvalue in enumerate(nums):
            if value + nextvalue == target:
                if idx != nextidx:
                    return [idx, nextidx]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for idx, num in enumerate(nums):
#             if target-num in nums:
#                 if idx != nums.index(target-num):
#                     return [idx, nums.index(target-num)]