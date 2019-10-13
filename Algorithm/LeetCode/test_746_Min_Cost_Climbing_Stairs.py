import pytest_watch

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
output = 6


def test_simple():
    assert solution(cost) == output

def solution(cost):
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return cost[0] if cost[0] > cost[1] else cost[1]
    dp = cost[0:2]
    for idx, value in enumerate(cost):
        if idx-2 >= 0:
            if cost[idx] + dp[idx-1] < cost[idx] + dp[idx-2]:
                dp.append(cost[idx] + dp[idx-1])
            else:
                dp.append(cost[idx] + dp[idx-2])
    if dp[-1] < dp[-2]:
        return dp[-1]
    else:
        return dp[-2]

if __name__ == "__main__":
    solution(cost)

"""
리팩토링하기
"""