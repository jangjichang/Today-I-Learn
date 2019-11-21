"""
Runtime: 556 ms, faster than 92.29% of Python online submissions for K Closest Points to Origin.
Memory Usage: 17.3 MB, less than 92.45% of Python online submissions for K Closest Points to Origin.
"""
import pytest_watch

points = [[3,3],[5,-1],[-2,4]]
K = 2
output = [[3,3],[-2,4]]

def test_simple():
    assert solution(points, K) == output

def solution(points, K):
    """
    O(nlogn)
    """
    return sorted(points, key=lambda x: x[0]**2+x[1]**2)[:K]


if __name__ == "__main__":
    print(solution(points, K))
    