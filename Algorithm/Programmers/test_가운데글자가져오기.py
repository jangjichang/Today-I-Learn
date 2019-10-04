import pytest_watch

input = "qwer"
output = "we"


def test_simple():
    assert solution(input) == output

def solution(input):
    return input[(len(input)-1)//2:len(input)//2+1]