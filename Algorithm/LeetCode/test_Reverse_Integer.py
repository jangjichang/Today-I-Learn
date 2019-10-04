import pytest_watch

input = 1534236469
output = 0


def test_simple():
    assert solution(input) == output

def solution(x):
    if x > 2**31-1:
        return 0
    elif x < -2**31:
        return 0
    output = ""
    x = int(x)
    if x < 0:
        output += "-"
        x *= -1
    x = str(x)
    x = x[::-1]
    output += x
    output = int(output)
    if output > 2**31-1:
        return 0
    elif output < -2**31:
        return 0
    return output

if __name__ == "__main__":
    solution(input)