"""
원소 길이를 key, 길이에 해당하는 원소를 value로 설정
각 key의 value들 중에 같은게 있는지 확인, 있으면 return false
key가 가장 큰 value들을 가장 작은 key의 길이로 split하고, 그 값이 해당 key의 value에 있는지 확인 있으면 return false
모든 작업을 마치고 return true

배열의
이를 배열의 처음부터 순회하면서 진행한다.

1. 배열을 원소의 길이를 기준으로 정렬한다.
2. n번째 원소를 기준으로 그 원소의 길이 만큼에 해당하는 값을 배열에 넣는다.
3. 이 배열에 n번째 원소가 있으면 return False
4. 이를 n+1 번째 부터 마지막 원소 까지 비교한다.
5. 반복문을 종료하고 return True
"""
phone_book = [["119", "97674223", "1195524421"],
              ["123", "456", "789"],
              ["12", "123", "1235", "567", "88"]]

result = [False,
          True,
          False]


def test_simple():
    # assert sol() == result
    for index, value in enumerate(phone_book):
        assert sol(value) == result[index]


def sol(pb):
    ans = list()
    pb = sorted(pb, key=lambda x: len(x))
    for index, value in enumerate(pb):
        prefix_check(pb, index, ans)
    if False in ans:
        return False
    return True


def prefix_check(pb, index, ans):
    for sub_value in pb[index+1:]:
        is_value_same(sub_value[:len(pb[index])], pb[index], ans)


def is_value_same(pivot, value, ans):
    if pivot == value:
        ans.append(False)


if __name__ == '__main__':
    sol(["119", "97674223", "1195524421"])
