array = [2, 3, 4, 5, 5, 5, 6, 1]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]

    less = []
    same = []
    bigger = []

    for i in array:
        if i > pivot:
            bigger.append(i)
        elif i < pivot:
            less.append(i)
        else:
            same.append(i)
    return quick_sort(less) + same + quick_sort(bigger)


def test_simple():
    assert quick_sort(array) == [1, 2, 3, 4, 5, 5, 5, 6]
