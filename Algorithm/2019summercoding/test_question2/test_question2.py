"""

"""
import pytest


def test_simple():
    assert ["()"] == solution(1)
    assert ["(())", "()()"] == solution(2)
    assert ["((()))", "(()())", "(())()", "()(())", "()()()"] == solution(3)
    assert ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"] == solution(4)


def pair_make(output, open, close, pairs, answer):
    if open == pairs and close == pairs:
        answer.append(output)
    else:
        if open < pairs:
            pair_make(output+'(', open+1, close, pairs, answer)
        if close < open:
            pair_make(output+')', open, close+1, pairs, answer)


def solution(N):
    answer = list()
    pair_make('', 0, 0, N, answer)
    return sorted(answer)
