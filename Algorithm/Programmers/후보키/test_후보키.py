from itertools import combinations
from collections import Counter

def the_number_of_foreignkey(relation):
    """가능한 모든 후보키 들을 생성하고 실제로 후보키가 될 수 있는지 확인한다.

    relation의 컬럼의 길이 만큼 조합을 한다.
    예를 들어 컬럼의 길이가 4라면, 후보키가 될 수 있는 것들은 1, 2, 3, 4개로 만든 조합들이다. 따라서

    인덱스로 따지면
    1개로 만든 것은 0, 1, 2, 3
    2개로 만든 것은 01, 02, 03, 12, 13, 23
    3개로 만든 것은 012, 013, 023, 123
    4개로 만든 것은 0123

    이 키들을 가지고 실제로 데이터를 셋에 저장했을 때 갯수가 같은지 확인한다.
    
    """
    possible_combinations = make_combination(len(relation[0]))
    answer = 0
    candidate_key = set()

    for combination in possible_combinations:
        if can_be_a_candidate_key(combination, candidate_key):
            relations = set()
            for rel in relation:
                row = ""
                for com in combination:
                    row += rel[com]
                relations.add(row)
            if len(relations) == len(relation):
                answer += 1
                candidate_key.add(combination)
    return answer


def make_combination(number):
    numbers = [i for i in range(number)]
    possible_combinations = list()

    for length in range(1, number+1):
        combination = combinations(numbers, length)
        for combination_ in combination:
            possible_combinations.append(combination_)
    
    return possible_combinations


def can_be_a_candidate_key(combination, candidate_keys):
    for candidate_key in candidate_keys:
        if not Counter(candidate_key) - Counter(combination):
            return False
    return True

def test_the_number_of_foreignkey():
    assert the_number_of_foreignkey([["100", "ryan", "music", "2"],
                                     ["200", "apeach", "math", "2"],
                                     ["300", "tube", "computer", "3"],
                                     ["400", "con", "computer", "4"],
                                     ["500", "muzi", "music", "3"],
                                     ["600", "apeach", "music", "2"]]) == 2
                                     

def test_make_combination():
    assert make_combination(3) == [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]


def test_can_be_a_candidate_key():
    assert can_be_a_candidate_key((1, 2), {(0, 1)}) == True
    assert can_be_a_candidate_key((0, 1), {(0, )}) == False
    # assert can_be_a_candidate_key((0, 1), set()) == True



if __name__ == '__main__':
    # the_number_of_foreignkey([["100", "ryan", "music", "2"],
    #                           ["200", "apeach", "math", "2"],
    #                           ["300", "tube", "computer", "3"],
    #                           ["400", "con", "computer", "4"],
    #                           ["500", "muzi", "music", "3"],
    #                           ["600", "apeach", "music", "2"]])
    can_be_a_candidate_key((1, 2), {(0, 1)})