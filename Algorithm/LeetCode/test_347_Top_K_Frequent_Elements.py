"""
Runtime: 84 ms, faster than 93.45% of Python online submissions for Top K Frequent Elements.
Memory Usage: 15.4 MB, less than 36.59% of Python online submissions for Top K Frequent Elements.
"""

import pytest_watch
import operator

nums = [4,1,-1,2,-1,2,3]
k = 2
output = [-1, 2]

def test_simple():
    assert solution(nums, k) == output

def solution(nums, k):
    answer = dict()

    for i in nums:
        try:
            answer[i] += 1
        except:
            answer[i] = 1
    
    sorted_answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

    answer = list()
    for i in sorted_answer:
        answer.append(i[0])
        if len(answer) >= k:
            return answer