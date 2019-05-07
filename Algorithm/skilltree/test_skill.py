import pytest_watch
import operator
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

"""
skill에 있는 원소들이 처음 나타난 인덱스를 구한다.
cbd -> 203
오름차순으로 정렬하면 bcd가 되므로 cbd랑 다르니까 이것은 불가능함

cbd -> 013
가능함

23 10 + index -> cb
가능함
"""

# skill = "CBD"
# skill_trees = "BDA"

def test_simple():
    assert 3 == solution(skill, skill_trees)


def solution(skill, skill_trees):
    counter = 0
    for skill_tree in skill_trees:
        skill_dict = {}
        for i, v in enumerate(skill):
            if v in skill_tree:
                 first_index = skill_tree.index(v)
                 skill_dict[v] = first_index
            else:
                first_index = i+ 100
                skill_dict[v] = first_index
        sorteddict = sorted(skill_dict.items(), key=operator.itemgetter(1))
        answer = ""
        for i in sorteddict:
            answer += i[0]
        if skill == answer:
            counter += 1
    return counter


if __name__ == '__main__':
    print(solution(skill, skill_trees))