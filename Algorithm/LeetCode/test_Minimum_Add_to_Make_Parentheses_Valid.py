"""
Runtime: 24 ms, faster than 24.40% of Python online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 11.8 MB, less than 20.00% of Python online submissions for Minimum Add to Make Parentheses Valid.
"""

import pytest_watch

S = ")()"
output = 1


def test_simple():
    assert solution(S) == output

def solution(S):
    stack = []
    answer = len(S)
    for i in S:
        if i == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
                answer -= 2
        else:
            stack.append(i)
    return answer