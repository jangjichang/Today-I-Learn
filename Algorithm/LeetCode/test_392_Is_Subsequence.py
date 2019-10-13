import pytest_watch

s, t = "aabc", 'yyayybyc'
output = False


def test_simple():
    assert solution(s, t) == output

def solution(s, t):
    stack = list([0])
    for i in s:
        try:
            idx = t[stack[-1]:].index(i) + stack[-1]
            stack.append(idx+1)
        except:
            return False
    return True


if __name__ == "__main__":
    solution(s, t)
