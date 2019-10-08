import pytest_watch

inputs = [2,7,9,3,1]
output = 12


def test_simple():
    assert solution(inputs) == output


def solution(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    dp = list()
    dp.append(nums[0])
    dp.append(nums[1])
    dp.append(max(dp[0]+nums[2], dp[1]))
    for i in range(3, len(nums)):
        dp.append(max(dp[i-2]+nums[i], dp[i-1], dp[i-3]+nums[i]))
    if dp[-1] > dp[-2]:
        return dp[-1]
    else:
        return dp[-2]
