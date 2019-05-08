import pytest
"""
대진표가 노출된 A를 보면서 B에서 출전할 사람을 구한다.
A, B를 정렬한다.
A의 요소들에 대해 다음을 확인한다.
B의 요소 중 그 요소보다 큰 수 중 A에서 가장 작은 수를 찾고 삭제한다. answer += 1
만약 그런 수가 없다면, 가장 작은 수를 찾고 삭제한다. answer += 0

A, B를 내림차순 정렬한다.
A와 B를 비교한다.
B가 A보다 작을 경우 

"""


def test_simple():
    assert 3 == solution([5, 1, 3, 7], [2, 2, 6, 8])
    assert 3 == solution([5, 4, 3, 2, 1], [4, 3, 2, 1, 1])
    assert 2 == solution([5, 4, 3, 3, 1], [1, 1, 4, 2, 3])
    assert 0 == solution([2, 2, 2, 2], [1, 1, 1, 1])


def solution(A, B):
    """
    answer = 0
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()
    loop_number = len(A)
    for i in range(0, loop_number):
        if A[0] < B[0]:
            index = 0
            while True:
                if index >= len(B):
                    B.pop()
                    answer += 1
                    break
                elif A[0] < B[index]:
                    index += 1
                elif A[0] >= B[index]:
                    B.pop(index-1)
                    answer += 1
                    break
            A.pop(0)
        else:
            B.pop()
            A.pop(0)
    return answer
    """

    """
    1 2 3 5 7
    2 2 6 8 9
    
    if a < b:
        remove a
        remove b
    else:
        
    
    3 5 7
    2 6 8
    
    3 5 7
    6 8
    
    2 2 2 2
    1 1 1 1
    """
    answer = 0
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()
    while A:
        if A[0] >= B[0]:
            del A[0]
        else:
            answer += 1
            del A[0]
            del B[0]
    return answer


if __name__ == '__main__':
    solution([5, 1, 3, 7], [2, 2, 6, 8])
    # solution([2, 2, 2, 2], [1, 1, 1, 1])
