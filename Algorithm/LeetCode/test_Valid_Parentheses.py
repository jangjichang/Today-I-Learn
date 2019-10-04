import pytest_watch

s = "()[]{}"
output = True


def test_simple():
    assert solution(s) == output

def solution(s):
    stack = list()
    for i in s:
        if i == ')':
            if not len(stack) or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif i == '}':
            if not len(stack) or stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif i == ']':
            if not len(stack) or stack[-1] != '[':
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    if len(stack):
        return False
    return True
