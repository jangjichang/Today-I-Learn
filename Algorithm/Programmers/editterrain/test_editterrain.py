import pytest

"""
현재 지형의 최고층과 최하층을 구한다.

최고층부터 최하층 범위까지 다음을 반복한다.

현재 지형의 모든 칸의 높이가 반복문의 그 층과 같기 위해 삭제, 추가해야하는 블록의 수를 각각 구한다.

블록을 삭제, 추가할 때 필요한 비용을 블록의 수와 곱한다.

반복문을 종료할 때 현재 저장한 최소 비용과 비교하여 작으면 갱신한다.
"""


def test_simple():
    assert 5 == solution([[1, 2], [2, 3]], 3, 2)
    assert 33 == solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3)


def solution(land, P, Q):
    max_floor = 0
    min_floor = 0
    min_answer = 999999
    for i in land:
        max_row = max(i)
        min_row = min(i)
        if max_row > max_floor:
            max_floor = max_row
        if min_row < min_floor:
            min_floor = min_row
    for target_floor in range(min_floor, max_floor+1):
        block_add = 0
        block_remove = 0
        for cur_floor in land:
            for height in cur_floor:
                if height > target_floor:
                    block_remove += (height - target_floor)
                else:
                    block_add += (target_floor - height)
        if min_answer > block_add*P + block_remove*Q:
            min_answer = block_add*P + block_remove*Q
    return min_answer


if __name__ == '__main__':
    solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3)
