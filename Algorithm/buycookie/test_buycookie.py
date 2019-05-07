import pytest

"""
배열의 0번째 인덱스 부터 다음과 같이 합을 비교한다.
시작위치와 끝 위치를 지정하고 왼쪽, 오른쪽으로 이동한다.
끝에 다다르면 반복문을 종료한다.

"""
def test_simple():
    assert 1 == 1


def solution(cookie):
    answer = 0
    if len(cookie) == 1:
        return 0
    elif len(cookie) == 2:
        if cookie[0] == cookie[1]:
            return cookie[0]
        else:
            return 0
    else:
        for i in range(len(cookie)):
            front_v = cookie[i]
            front_i = i
            front_sum = front_v
            back_v = cookie[i+1]
            back_i = i+1
            back_sum = back_v
            while(True):
                if front_i == 0 or back_i == len(cookie):
                    break




