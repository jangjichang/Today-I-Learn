import pytest_watch


def test_simple():
    assert "0" == solution([0, 0, 0, 0])
    assert "40403" == solution([403, 40])
    assert "40540" == solution([40, 405])
    assert "40440" == solution([40, 404])
    assert "12121" == solution([12, 121])
    assert "223222" == solution([2, 22, 223])
    assert "21221" == solution([21, 212])
    assert "41541" == solution([41, 415])
    assert "1000000" == solution([1000, 0, 0, 0])
    assert "70000" == solution([70, 0, 0, 0])
    assert "222" == solution([2, 22])
    assert "121312" == solution([12, 1213])
    assert "1" == solution([1])
    assert "0" == solution([0, 0])


def compare_value(first, second):
    if len(str(first)) == len(str(second)):
        if first > second:
            return first
        else:
            return second
    else:
        if int(str(first) + str(second)) >= int(str(second) + str(first)):
            return first
        return second


def my_quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        less = []
        same = []
        bigger = []
        for i in numbers:
            if i == numbers[0]:
                same.append(i)
            elif compare_value(i, numbers[0]) == numbers[0]:
                bigger.append(i)
            else:
                less.append(i)
        return my_quick_sort(less) + same + my_quick_sort(bigger)


def solution(numbers):
    for j in numbers:
        if j != 0:
            answer = my_quick_sort(numbers)
            str_answer = ""
            for i in answer:
                str_answer = str_answer + str(i)
            return str_answer
        else:
            return "0"


if __name__ == '__main__':
    numbers = [403, 40]
    print(solution(numbers))
    # pass
