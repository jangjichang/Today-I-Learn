import pytest_watch

priorities = [1, 1, 9, 1, 1, 1]	
location = 0
output = 5


def test_simple():
    assert solution(priorities, location) == output

"""
[[2, 1, 3, 2],
[0, 1, 2, 3]]

[[1, 3, 2, 2],
[1, 2, 3, 0]]

[[3, 2, 2, 1],
[2, 3, 0, 1]]

전체 len - 현재 len + 1

[[1, 1, 9, 1, 1, 1],
[0, 1, 2, 3, 4, 5]]

[[1, 9, 1, 1, 1, 1],
[1, 2, 3, 4, 5, 0]]

[[9, 1, 1, 1, 1, 1],
[2, 3, 4, 5, 0, 1]]

[[1, 1, 1, 1, 1],
[3, 4, 5, 0, 1]]

[[1, 1, 1, 1],
[4, 5, 0, 1]]

[[1, 1, 1],
[5, 0, 1]]

[[1, 1],
[0, 1]]

전체 len - 현재 len + 1
6 - 2 + 1 = 5

"""

"""
123

231

a[:-1]
"""

def sol(priority_2d, location):
    if priority_2d[0][0] == max(priority_2d[0]) and priority_2d[1][0] == location:
        return len(priorities) - len(priority_2d[0]) + 1
    if priority_2d[0][0] == max(priority_2d[0]):
        priority_2d[0].pop(0)
        priority_2d[1].pop(0)
        return sol(priority_2d, location)
    priority_2d[0] = priority_2d[0][1:] + priority_2d[0][:1]
    priority_2d[1] = priority_2d[1][1:] + priority_2d[1][:1]
    return sol(priority_2d, location)


def solution(priorities, location):
    priority_2d = [priorities, [i for i in range(len(priorities))]]
    return sol(priority_2d, location)


if __name__ == "__main__":
    solution(priorities, location)
