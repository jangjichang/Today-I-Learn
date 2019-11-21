"""
Runtime: 32 ms, faster than 91.90% of Python online submissions for Valid Anagram.
Memory Usage: 13 MB, less than 50.00% of Python online submissions for Valid Anagram.
"""

import pytest_watch

s = "anagram"
t = "nagaram"
output = True


def test_simple():
    assert solution(s, t) == output

def solution(s, t):
    answer = dict()
    for i in s:
        try:
            answer[i] += 1
        except:
            answer[i] = 1
    
    for i in t:
        try:
            if answer[i] > 1:
                answer[i] -= 1
            else:
                answer.pop(i)
        except:
            return False
    return not bool(answer)

if __name__ == "__main__":
    print(solution(s, t))