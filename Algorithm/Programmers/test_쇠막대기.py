import pytest_watch

arrangement = "()(((()())(())()))(())"
output = 17

def test_simple():
    assert solution(arrangement) == output

"""
()(((()())(())()))(())

..(((....)(..)..))(..)


"""

def solution(arrangement):
    arrangement = arrangement.replace('()', '.')
    stick = list()
    answer = 0
    for i in arrangement:
        if i == '(':
            stick.append('(')
        elif i == ')':
            stick.pop()
            answer += 1
        elif i == '.':
            answer += len(stick)
    return answer


    """
    시간 초과
    """
    # arrangement = arrangement.replace('()', '..')
    # stick_idx = list()
    # stick = list()
    # for idx, value in enumerate(arrangement):
    #     if value == '(':
    #         stick.append((idx, value))
    #     if value == ')':
    #         stick_idx.append((stick.pop()[0], idx))
    
    # count = 0
    # flag = 0
    # for idx in stick_idx:
    #     for element in arrangement[idx[0]:idx[1]]:
    #         if element == '.':
    #             count += 1
    #             flag = 1
    #     if flag == 1:
    #         count += 2
    #         flag = 0
    # return count // 2


if __name__ == "__main__":
    solution(arrangement)
