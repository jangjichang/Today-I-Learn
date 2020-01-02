def solution(arr):
    different_numbers = arr[0:1]
    for number in arr[1:]:
        if different_numbers[-1] != number:
            different_numbers.append(number)
    return different_numbers

def test_solution():
    assert solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1]
    assert solution([4, 4, 4, 3, 3]) == [4, 3]

    assert solution([]) == []
    assert solution([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution([0, 0, 0, 0]) == [0]
    
    