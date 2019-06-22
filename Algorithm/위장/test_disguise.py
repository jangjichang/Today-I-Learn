"""
해결 방법이 생각나지 않아 구글링함...
왜 아직도 (n 종류의 옷 가지수 +1) * (n+1 종류의 옷 가지수 +1) ... -1이 정답인지 모르겠음 
"""
from collections import Counter

clothes = [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
           [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]]
results = [5, 3]


def test_simple():
    for i in range(len(clothes)):
        solution(clothes[i]) == results[i]


def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer


