"""
Runtime: 32 ms, faster than 80.90% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12 MB, less than 15.38% of Python online submissions for Intersection of Two Arrays II.
"""

import pytest_watch

# nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
# output = [4, 9]
nums1, nums2 = [1, 2, 2, 1], [2, 2]
output = [2, 2]


def test_simple():
    assert solution(nums1, nums2) == output

def solution(nums1, nums2):
    nums1_dict = {}
    answer = []
    for i in nums1:
        try:
            nums1_dict[i] += 1
        except:
            nums1_dict[i] = 1
    for i in nums2:
        try:
            if nums1_dict[i] >= 1:
                nums1_dict[i] -= 1
                answer.append(i)
        except:
            pass
    return answer
