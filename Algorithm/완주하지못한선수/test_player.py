# import pytest_watch
from collections import Counter

participant = [["leo", "kiki", "eden"],
               ["marina", "josipa", "nikola", "vinko", "filipa"],
               ["mislav", "stanko", "mislav", "ana"]]

completion = [["eden", "kiki"],
              ["josipa", "filipa", "marina", "nikola"],
              ["stanko", "ana", "mislav"]]

answer = ["leo",
          "vinko",
          "mislav"]


def test_simple():
    for i in range(3):
        assert solution(participant[i], completion[i]) == answer[i]


def solution(p, c):
    # p = Counter(p)
    # c = Counter(c)
    # p.subtract(c)
    # print(p)
    # for key, value in p.items():
    #     if value == 1:
    #         return key
    # answer = Counter(p) - Counter(c)
    return list((Counter(p) - Counter(c)).keys())[0]


if __name__ == '__main__':
    solution(participant[0], completion[0])
