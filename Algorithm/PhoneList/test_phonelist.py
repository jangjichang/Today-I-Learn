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
    c = [i[0] for i in pb]
    c = Counter(c)
    for key, value in c.items():
        if c[key] >= 2:
            return False
    return True
