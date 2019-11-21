import pytest_watch

s1, s2 = 'xczvup', 'hdalwr'
output = False

def test_simple():
    assert string_dict(s1, s2) == output

# Brute Force
def brute_force(s1, s2):
    """
    Time Complexity: O(n**2)
    """
    for i in s1:
        for j in s2:
            if i == j:
                return True
    return False

# using hash
def string_dict(s1, s2):
    s1_dict = dict()
    s2_dict = dict()
    
    for i in s1:
        s1_dict[i] = 1

    for j in s2:
        if s1_dict.get(j) is not None:
            return True
    return False
        