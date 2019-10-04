import pytest_watch


def test_simple():
    assert 7 == solution("ULURRDLLU")
    assert 7 == solution("LULLLLLLU")
    assert 1 == solution("L")
    assert 5 == solution("LLLLLLLLLLLLL")
    assert 2 == solution("UDRLUDRLUDRL")


"""
게임 캐릭터가 지나가는 길을 표현하는 방법을 정한다.
(0, 0) -> (0, 1)로 이동하는 길은 "0001"로 표현한다.
(0, 1) -> (0, 0)로 이동하는 길도 "0001"로 표현한다.
작은 문자열을 앞에 표현함.

캐릭터가 지나가는 길을 표현하고 길을 set에 넣는다.
set의 크기를 반환한다.

예외 상황
캐릭터가 지나가는 위치가 좌표 평면이기 때문에 크기를 비교한다.
(5, 0)에서 R 일 경우 (6, 0)이 아니라, (5, 0)이어야한다.
(5 ,5)에서 U 일 경우 (5, 6)이 아니라, (5, 5)이어야한다.
"""
def loc_valid(loc):
    if loc[0] <= 5 and loc[0] >= -5 and loc[1] <= 5 and loc[1] >= -5:
        return True
    else:
        return False


def solution(dirs):
    directions = {"U": (0, 1),
                  "D": (0, -1),
                  "R": (1, 0),
                  "L": (-1, 0)}
    loc = (0, 0)
    load = set()
    for i in dirs:
        new_loc = (loc[0] + directions[i][0], loc[1] + directions[i][1])
        if loc_valid(new_loc):
            load.add(loc + new_loc)
            load.add(new_loc + loc)
            loc = new_loc
    return len(load)//2


if __name__ == '__main__':
    print(solution("ULURRDLLU"))
