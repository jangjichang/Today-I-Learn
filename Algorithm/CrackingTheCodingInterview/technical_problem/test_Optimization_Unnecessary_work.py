"""
예제: a, b, c, d가 1에서 1000 사이에 있는 정수 값 중 하나일 때 a^3 + b^3 = c^3 + d^3을 만족하는 모든 자연수를 출력하시오.
"""
import pytest_watch

input = 1000


def test_simple():
    assert solution_brute_force(input)


def solution_brute_force(input):
    """
    시간 복잡도: O(n^4)
    """
    for a in range(1, input):
        for b in range(1, input):
            for c in range(1, input):
                for d in range(1, input):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)
                        

def solution_remove_unnecessary_work(input):
    """
    시간 복잡도: O(n^4)
    가능한 d의 rkqtdms 딱 하나뿐이기 때문에 d for loop에 break를 추가했다.
    하지만 여전히 시간 복잡도는 같음
    """
    for a in range(1, input):
        for b in range(1, input):
            for c in range(1, input):
                for d in range(1, input):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)
                        break


def solution_mathematical(input):
    """
    시간 복잡도: O(n^3)
    """
    for a in range(1, input):
        for b in range(1, input):
            for c in range(1, input):
                d = (pow(a**3 + b**3 - c**3, 1/3))
                if isinstance(d, complex):
                    pass
                else:
                    d = int(d)
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)


if __name__ == "__main__":
    # print(solution_brute_force(input))
    # print(solution_remove_unnecessary_work(input))
    print(solution_mathematical(input))

