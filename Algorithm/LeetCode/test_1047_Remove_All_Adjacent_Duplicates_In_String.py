import pytest_watch

input = "abbaca"
output = "ca"


def test_simple():
    assert solution(input) == output


"""
input에 있는 원소를 스택에 하나씩 넣는다.
넣을때 top에 있는 원소와 같으면 삭제한다.
"""


def solution(S):
    stack = list()
    for i in S:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return ''.join(stack)


if __name__ == "__main__":
    pass
