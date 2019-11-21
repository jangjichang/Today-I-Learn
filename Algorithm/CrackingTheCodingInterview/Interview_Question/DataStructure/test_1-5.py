import pytest_watch

s1, s2 = ['pale', 'pales', 'pale', 'pale'], ['ple', 'pale', 'bale', 'bake']
output = [True, True, True, False]


def test_simple():
    for i, j, k in zip(s1, s2, output):
        assert solution(i, j) == k


def solution(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1)-len(s2)) > 1:
        return False
    diff = 0
    short_list = min(s1, s2, key=len)
    if short_list == s1:
        long_list = s2
    else:
        long_list = s1
    
    if len(short_list) == len(long_list):
        idx = 0
        while idx < len(short_list):
            if short_list[idx] != long_list[idx]:
                diff += 1
            if diff >= 2:
                return False
            idx += 1
        return True
    
    else:
        short_idx = 0
        long_idx = 0
        while short_idx < len(short_list):
            if short_list[short_idx] != long_list[long_idx]:
                diff += 1
                long_idx += 1
            else:
                long_idx += 1
                short_idx += 1
            if diff >= 2:
                return False
        return True
