import re
import math
import copy

test1 = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2']
test2 = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']
answer = [16384, 65536, 43690, 65536]


def solution(str1, str2):
    group1 = makeToken(str1)
    group2 = makeToken(str2)
    if not group1 and not group2:
        return 65536
    intersection = makeIntersection(group1, group2)
    union = makeUnion(group1, group2, intersection)
    answer = math.floor((len(intersection) / len(union)) * 65536)
    return answer


def makeToken(input):
    str = copy.deepcopy(input)
    str = str.lower()
    p = re.compile('[a-z]{2}')
    temp = []
    for i in range(len(str)-1):
        if p.match(str[i:i+2]):
            temp.append(str[i:i+2])
    return temp


def makeIntersection(input1, input2):
    new_input1 = copy.deepcopy(input1)
    new_input2 = copy.deepcopy(input2)
    copy_new_input1 = copy.deepcopy(input1)
    intersection = []

    # 반복문 중간에 반복하는 배열의 원소를 지우는 것은 상당히 위험한 일이다.
    for i in copy_new_input1:
        if i in new_input2:
            intersection.append(i)
            new_input2.remove(i)
    return intersection


def makeUnion(input1, input2, input3):
    new_input1 = copy.deepcopy(input1)
    new_input2 = copy.deepcopy(input2)
    new_input3 = copy.deepcopy(input3)
    new_input1.extend(new_input2)

    for i in new_input3:
        new_input1.remove(i)
    return new_input1

for i in range(4):
    print(answer[i] == solution(test1[i], test2[i]))
