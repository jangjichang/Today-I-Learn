import pytest_watch

S = "a##c"
T = "#a#c"
output = True

def test_simple():
    assert solution(S, T) == output

def solution(S, T):
    output1 = list()
    output2 = list()
    for i in S:
        if i == '#':
            if output1:
                output1.pop()
        else:
            output1.append(i)
    for i in T:
        if i == '#':
            if output2:
                output2.pop()
        else:
            output2.append(i)
    if output1 == output2:
        return True
    return False