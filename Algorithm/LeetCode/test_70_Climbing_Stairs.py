import pytest_watch

input = 3
output = 3

"""
4
1+1+2
2+2

1+1+1+1
1+2+1
2+1+1
"""
def test_simple():
    assert solution(input) == output


def solution(input):
    dp = [0, 1, 2]
    for i in range(3, input+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[input]

