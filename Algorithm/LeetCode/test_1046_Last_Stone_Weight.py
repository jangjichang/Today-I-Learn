"""
Runtime: 12 ms, faster than 96.10% of Python online submissions for Last Stone Weight.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Last Stone Weight.
"""

import pytest_watch

stones = [2,7,4,1,8,1]
output = 1


def test_simple():
    assert solution(stones) == output

def solution(stones):
    while len(stones) > 1:
        stones.sort()
        heaviest = stones.pop()
        next_heaviest = stones.pop()

        if heaviest == next_heaviest:
            pass
        else:
            stones.append(heaviest-next_heaviest)
    if stones:
        return stones[0]
    return 0
        
