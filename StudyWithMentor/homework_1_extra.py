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
import unittest


input = list(range(1, 5001))
output = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97, 108, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 211,
         222, 233, 244, 255, 266, 277, 288, 299, 310, 312, 323, 334, 345, 356, 367, 378, 389, 400, 411, 413, 424, 435,
         446, 457, 468, 479, 490]
list_result = list(range(1, 491))


def generator(n):
    str_n = str(n)
    result = n
    for i in str_n:
        result += int(i)
    return result


def self_number_generator(input):
    for i in input:
        generator_result = generator(i)
        if generator_result in list_result:
            list_result.remove(generator_result)


class SelfNumberTest(unittest.TestCase):
    def self_number_test(self):
        self_number_generator(input)
        self.assertEqual(list_result, output)


if __name__ == '__main__':
    unittest.main()

self_number_generator(input)
print(list_result)








