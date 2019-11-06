"""
예제: 서로 다른 정수로 이루어진 배열이 있을 때 두 정수의 차이가 k인 쌍의 개수를 세라. 예를 들어 주어진 배열이 [1, 7, 5, 9, 2, 12, 3]이고 k=2이면, 두 정수의 차이가 2인 쌍은 다음과 같이 네개가 존재한다. [1, 3], [3, 5], [5, 7], [7, 9]
"""
import pytest_watch

input = [1, 7, 5, 9, 2, 12, 3]
k = 2
output = 4


def test_simple():
    assert solution_brute_force(input, k) == output
    assert solution_sort_and_search(input, k) == output
    assert solution_hash_table(input, k) == output


def solution_brute_force(input, k):
    """
    시간 복잡도: O(n^2)
    """
    output = set()
    for i in input:
        for j in input:
            if i - j == k or i - j == -k:
                output.add(tuple(sorted([i, j])))
    return len(output)


def solution_sort_and_search(input, k):
    """
    시간 복잡도: O(nlogn)
    """
    output = set()
    input.sort()
    for i in input:
        try:
            input.index(i-k)
            output.add(tuple(sorted([i, i-k])))
            input.index(i+k)
            output.add(tuple(sorted([i, i+k])))
        except:
            pass
    return len(output)


def solution_hash_table(input, k):
    """
    시간 복잡도: O(n)
    """
    output = set()
    hash_table = dict()
    for i in input:
        hash_table[i] = i
    for i in input:
        try:
            j = hash_table.get(i-k, False)
            if j:
                output.add(tuple(sorted([i, j])))
            j = hash_table.get(i+k, False)
            if j:
                output.add(tuple(sorted([i, j])))
        except:
            pass
    return len(output)

if __name__ == "__main__":
    print(solution_hash_table(input, k))
