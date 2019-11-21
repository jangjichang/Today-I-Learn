import pytest_watch

s1, s2 = "aabcd", "abd"
output = True

def test_simple():
    assert solution(s1, s2) == output

def solution(s1, s2):
    s_dict = dict()
    longer_string = max(s1, s2, key=len)

    if longer_string == s1:
        shorter_string = s2
    else:
        shorter_string = s1

    for i in longer_string:
        try:
            s_dict[i] += 1
        except:
            s_dict[i] = 1
    
    for i in shorter_string:
        try:
            s_dict[i] -= 1
            if s_dict[i] < 0:
                return False
        except:
            return False
    return True