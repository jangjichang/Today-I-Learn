import pytest_watch

input = [-2, 1, -3, 4, -1, 2, 1, -5, 4, -1, -1]
output = 6

"""
구글링함
i번째 원소에 대해
i번 이전의 연속합 + i번째 원소 vs i번째 원소 큰 값 가져옴

dp [-2, 1, -2, 4, 3, 5, 6, 1, 5, 4, 3]

"""

def test_simple():
    assert solution(input) == output


def solution(nums):
    output = nums[0]
    max = nums[0]
    dp = nums[:1]
    for idx, value in enumerate(nums[1:]):
        if value > dp[idx] + value:
            dp.append(value)
            output = value
            if output > max:
                max = output
        else:
            dp.append(dp[idx]+value)
            output = dp[idx]+value
            if output > max:
                max = output
    return max
        

if __name__ == "__main__":
    solution(input)