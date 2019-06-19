"""
원소 길이를 key, 길이에 해당하는 원소를 value로 설정
각 key의 value들 중에 같은게 있는지 확인, 있으면 return false
key가 가장 큰 value들을 가장 작은 key의 길이로 split하고, 그 값이 해당 key의 value에 있는지 확인 있으면 return false
모든 작업을 마치고 return true

배열의
이를 배열의 처음부터 순회하면서 진행한다.
"""

from collections import Counter

phone_book = [["119", "97674223", "1195524421"],
              ["123", "456", "789"],
              ["12", "123", "1235", "567", "88"]]

result = [False,
          True,
          False]


def test_simple():
    for index, value in enumerate(phone_book):
        assert solution(value) == result[index]

def solution(pb):
    # c = [i[0] for i in pb]
    # c = Counter(c)
    # for key, value in c.items():
    #     if c[key] >= 2:
    #         return False
    # return True
