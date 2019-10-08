import pytest_watch

input = [1, 2]
output = 1


def test_simple():
    assert solution(input) == output


def solution(prices):
    if not prices:
        return 0
    buy = prices[0]
    sell = prices[0]
    max = 0
    for i in prices:
        if buy > i:
            buy = i
            sell = i
        if sell < i:
            sell = i
        if max < sell-buy:
            max = sell-buy
    return max


if __name__ == "__main__":
    solution(input)
