import pytest

input = list(range(1, 24))
output = [2, 4, 6, 8, 10, 12, 14, 16, 18, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 22, 24, 26, 28]


# pytest를 이용해 testcase에 대해 함수 d의 결과값이 output과 같은지 확인
# def Test_simple():
#     for i in input:
#         assert output[i-1] == d(i)
#     assert 1 == 2


# n의 각 자리 숫자와 n의 합을 구한다.
def d(n):
    sum_of_digit = n
    for i in str(n):
        sum_of_digit += int(i)
    return sum_of_digit


# 숫자를 입력하면 1부터 입력한 숫자까지의 self number를 list로 반환합니다.
def get_self_number(limit):
    limit += 1
    number_list = list(range(1, limit))

    for i in range(1, limit):
        if d(i) in number_list:
            number_list.remove(d(i))
    return sum(number_list)


print(get_self_number(5000))



"""
1. input과 ouput을 충분히 모아보세요. 처음부터 완벽할 필요는 없고, 코딩 도중에 추가하셔도 됩니다.
d(1) = 1 + 1 = 2
d(2) = 2 + 2 = 4
d(3) = 3 + 3 = 6
d(4) = 4 + 4 = 8
d(5) = 5 + 5 = 10
d(6) = 6 + 6 = 12
d(7) = 7 + 7 = 14
d(8) = 8 + 8 = 16
d(9) = 9 + 9 = 18
d(10) = 1 + 0 + 10 = 11
d(11) = 1 + 1 + 11 = 13
d(12) = 1 + 2 + 12 = 15
d(13) = 1 + 3 + 13 = 17
d(14) = 1 + 4 + 14 = 19
d(15) = 1 + 5 + 15 = 21
d(16) = 1 + 6 + 16 = 23
d(17) = 1 + 7 + 17 = 25
d(18) = 1 + 8 + 18 = 27
d(19) = 1 + 9 + 19 = 29
d(20) = 2 + 0 + 20 = 22
d(21) = 2 + 1 + 21 = 24
d(22) = 2 + 2 + 22 = 26
d(23) = 2 + 3 + 23 = 28
...


2. 어떻게 풀어볼지 간단히 생각하고, 곰인형 등을 앞 또는 옆에 두고 친절하게 설명해 보세요.
A. 우선 1부터 5000까지의 배열을 만든다.
B. 1부터 5000까지의 수를 d()함수에 입력하고 출력된 값을 배열에서 지운다.
C. B단계가 끝나면 A에서 만든 배열에는 self number가 남는다.
D. A단계에서 만든 배열의 원소의 합을 구한다.
  

3. 어떻게 하면 1번에서 모은 input과 output을 항상 순식간에 확인할 수 있을지 고민해 보세요.(사실 그냥 자동화된 테스트 코드를 작성하면
 됩니다).
1번에서 모은 input과 output을 배열에 저장하고 d 함수에 input 값을 넣은 결과를 result라는 배열에 저장하고 output과 비교한다.

4. 구현합니다.

5. 공유합니다.
"""

"""
코딩 테스트를 준비해야 하는 분들은 이 문제를 풀어보세요.

자연수 n이 있을 때 함수 d는 n의 각 자리 숫자와 n의 합을 구한다.

예를 들어, d(91) = 9 + 1 + 91 = 101 이 된다.

이때 n을 d(n)의 generator라고 한다.

예를 들어, 91은 101의 generator다.

generator가 없는 숫자를 self number라고 하고, 1, 3, 5, 7, 9, 20, 31 등이 여기에 속한다.

1 이상, 5000 미만의 self number의 합을 구하는 프로그램을 만들자.

코딩 전에 다음 순서를 확인하세요.

1. input과 ouput을 충분히 모아보세요. 처음부터 완벽할 필요는 없고, 코딩 도중에 추가하셔도 됩니다.
2. 어떻게 풀어볼지 간단히 생각하고, 곰인형 등을 앞 또는 옆에 두고 친절하게 설명해 보세요.
3. 어떻게 하면 1번에서 모은 input과 output을 항상 순식간에 확인할 수 있을지 고민해 보세요(사실 그냥 자동화된 테스트 코드를 작성하면 됩니다).
4. 구현합니다.
5. 공유합니다.
"""

"""
피드백
1. output은 어떻게 구하신 건가요? 만약 프로그램을 돌려서 얻은 값이라면 그게 맞는지 어떻게 확신할 수 있을까요?
>> output은 wikipedia에서 구했습니다. (https://en.wikipedia.org/wiki/Self_number?fbclid=IwAR2CNZSppbKcaGbZGIp3Cfm4e2FoIspy9d5oxxLfqf068CYT48TFqXVbpr0)

2. SelfNumberTest에서 참조하는 input과 output이 너무 멀리 떨어져 있습니다. 이 코드를 읽는 사람은 이걸 통해 뭔가를 알기 어렵죠. 뭔지 모르겠지만 뭔가 확인하겠거니 하고 넘어갈 가능성이 큽니다. 어떻게 해야 이 코드를 읽는 사람이 깊이 생각하지 않아도 이 부분을 쉽게 이해하는데 도움을 줄 수 있을까요?
>> pytest를 이용해 test코드를 다시 작성했습니다. 테스트를 하는 test 함수를 intput, output 바로 밑에 작성하였습니다.
 
3. 사용자가 self number의 합을 구하고 싶다면 어떤 함수를 호출해야 할까요? 지금은 사용자가 전체 코드를 열심히 분석해서 나만의 self number 구하는 코드를 다시 작성해야 합니다.
get_self_number함수를 작성하였습니다. 이 함수는 인자로 limit을 받아 1부터 limit까지의 self number의 합을 반환합니다.
"""







