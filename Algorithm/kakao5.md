# 문제
[카카오 클러스터링](https://programmers.co.kr/learn/courses/30/lessons/17677)

# 해설

1. 입력으로 들어오는 문자열을 두 글자씩 끊어서 다중집합의 원소로 만든다.
2. 교집합과 합집합을 구한다.
3. 자카드 유사도를 출력한다.

문자열을 두 글자씩 끊어서 다중집합의 원소로 만든다. 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우 글자 쌍을 버리므로 정규식을 이용해 확인한다.

```
# 정규식 사용을 위해 re 모듈을 임포트합니다.
import re
# deepcopy 사용을 위해 copy 모듈을 임포트합니다.
import copy

# 문자열을 두 글자씩 끊는 함수입니다.
def makeToken(input):
    str = copy.deepcopy(input)
    str = str.lower()
    # 정규식 사용법입니다. 패턴을 정합니다. '소문자 2개'가 패턴이 되겠네요
    p = re.compile('[a-z]{2}')
    temp = []
    for i in range(len(str)-1):
        # 두 글자씩 패턴에 매칭이 되는지 확인합니다. 매칭이 되면 match 객체가 리턴되고
        # 아니면 None이 리턴됩니다.
        if p.match(str[i:i+2]):
            temp.append(str[i:i+2])
    return temp
```

교집합과 합집합을 구합니다.
```
# 교집합을 구하는 함수입니다.
def makeIntersection(input1, input2):
    new_input1 = copy.deepcopy(input1)
    new_input2 = copy.deepcopy(input2)
    copy_new_input1 = copy.deepcopy(input1)
    intersection = []

    # 반복문 중간에 반복하는 배열의 원소를 지우는 것은 상당히 위험한 일이다.
    # 그래서 참고할 리스트를 하나 생성했다 (copy_new_input1)
    for i in copy_new_input1:
        if i in new_input2:
            intersection.append(i)
            new_input2.remove(i)
    return intersection

# 합집합을 구하는 함수입니다.
def makeUnion(input1, input2, input3):
    new_input1 = copy.deepcopy(input1)
    new_input2 = copy.deepcopy(input2)
    new_input3 = copy.deepcopy(input3)
    new_input1.extend(new_input2)

    for i in new_input3:
        new_input1.remove(i)
    return new_input1
```

자카드 유사도 구하기
```
import math
# floor 사용을 위해 math를 import합니다.
def solution(str1, str2):
    group1 = makeToken(str1)
    group2 = makeToken(str2)
    # 공집합이면 65536을 출력합니다.
    if not group1 and not group2:
        return 65536
    intersection = makeIntersection(group1, group2)
    union = makeUnion(group1, group2, intersection)
    # 자카드 유사도 값을 구합니다.
    # 요구사항대로 값에 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력합니다.
    answer = math.floor((len(intersection) / len(union)) * 65536)
    return answer
```
# 소감
문제는 상당히 쉬웠다.

생각한대로 코딩만 하면되는 문제다.

근데 이 문제를 풀면서 기본기가 아직 부족하다는 걸 느꼈고 많이 배웠다.(???)

- python은 call by value, call by reference도 아니고 [**call by object reference**](https://item4.github.io/2015-07-18/Some-Ambiguousness-in-Python-Tutorial-Call-by-What/)이다. 이것 때문에 deepcopy를 썼는데 deepcopy안쓰고 다시 구현해야겠다.
- 정규식 사용 방법을 익혔다. (정규식)[https://regexone.com/]
```
import re
data = "python"
p = re.compile('[a-z]{2}')
m = p.match(data)
```
문자 클래스 []
-> 문자 클래스로 만들어진 정규식은 '['와 ']' 사이의 문자들과 매치라는 의미를 갖는다.

예를 들어, [abc]는 a, b, c 중 한 개의 문자와 매치를 의미한다.

문자 클래스 안에 '-'가 있는 경우는 범위를 의미한다.

예를 들어, [0-9]는 0,1,2, ... ,8, 9 즉 0부터 9까지의 숫자와 매치를 의미한다.

알파벳 매치를 사용하고 싶을 때 [a-Z], [a-z], [A-Z] 등을 사용하고 한글은 [가-힣]를 사용한다.

|Method  |목적  |
|---|---|
|match()   |문자열의 처음부터 정규식과 매치되는지 조사한다.   |
|search()   |문자열 전체를 검색하여 정규식과 매치되는지 조사한다.   |
|findall()   |정규식과 매치되는 모든 문자열을 리스트로 리턴한다.   |
|finditer()   |정규식과 매치되는 모든 문자열을 iterator 객체로 리턴한다.   |
|sub()   |정규식과 매치되는 문자열을 변환한다.   |
|split()   |정규식을 기준으로 문자열을 나눈다.   |

연습문제: 휴대전화 뒷 4자리만 바꿔서 출력하기
```
import re

data = """
park 010-1234-5678
kim  010-9101-1112
"""

p = re.compile('(\d{3}[-]\d{4}[-])\d{4}')
answer = p.sub('\g<1>****', data)

print(answer)

```
휴대전화 뒷 4자리만 바꿔서 출력하기 위해서는 우선 휴대전화와 매치되는 정규식을 구해야한다.
휴대전화 패턴은 숫자 3개, 하이픈(-), 숫자 4개, 하이픈(-), 숫자 4개로 구성된다.

이를 정규표현식으로 나타내면 다음과 같다.
'\d{3}[-]\d{4}[-]\d{4}'

그런데 여기서 문제가 있다. 휴대전화가 매칭되는 것을 찾고 모든 문자열을 바꾸는 것이 아니라 뒤에 4자리만 바꿔야한다. 뒷 4자리만 바꾸기 위해 group이라는 것을 사용한다.

'(\d{3}[-]\d{4}[-])\d{4}'

괄호를 사용하여 그룹화 하면 괄호안에 있는 내용들을 그대로 불러 올 수 있다.

\g<1>로 첫번째 그룹에 해당되는 내용을 가져온다.

처음에 어떻게 앞쪽 번호를 가져올까 찾아보다가 발견했다.

근데 왜 \g<1>을 쓰는지 궁금해서 python console에서 어떤 데이터가 담겨있는지 확인해봤다.

```
import re

data = """
park 010-1234-5678
kim  010-9101-1112
"""

p = re.compile('(\d{3}[-]\d{4}[-])\d{4}')
s = p.search(data)

# s.regs
# ((6, 19), (6, 15))
```
s.regs의 0번째 값은 정규표현식과 매칭되는 전체 문자열의 인덱스이고
s.regs의 1번째 값은 첫번째 그룹의 인덱스인 것을 확인할 수 있다.
그래서 첫번째 인덱스의 값을 그대로 가져와서 출력하기 위해 \g<1>을 사용했다.


- 반올림 사용 방법을 익혔다.
# 내일 정리
```
import math

```
