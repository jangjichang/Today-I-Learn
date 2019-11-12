"""
Runtime: 28 ms, faster than 41.42% of Python online submissions for Score After Flipping Matrix.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Score After Flipping Matrix.
"""
import pytest_watch

A = [[0, 0, 1, 1],
     [1, 0, 1, 0],
     [1, 1, 0, 0]]

output = 39


def test_simple():
    assert solution(A) == output


def solution(A):
    for row in A:
        if row[0] == 0:
            for idx in range(len(row)):
                row[idx] ^= 1

    for i in range(1, len(A[0])):
        nums_of_zero = 0
        nums_of_one = 0
        for j in range(len(A)):
            if A[j][i] == 0:
                nums_of_zero += 1
            else:
                nums_of_one += 1
        if nums_of_zero > nums_of_one:
            for k in range(len(A)):
                A[k][i] ^= 1
    answer = 0

    for rows in A:
        s = [str(i) for i in rows]
        answer += int("".join(s), 2)
    return answer




if __name__ == "__main__":
    solution(A)
