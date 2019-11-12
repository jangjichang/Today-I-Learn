import pytest_watch

N = 5
answer = 26


def test_simple():
    assert solution(N) == answer

def solution(N):
    fibo = [1, 1]
    for i in range(2, N):
        try:
            fibo.append(fibo[i-2] + fibo[i-1])
        except:
            pass
    return (2*fibo[-1] + fibo[-2]) * 2
