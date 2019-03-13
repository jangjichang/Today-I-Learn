"""
사칙연산 계산기 만들기
1+3을 입력하면 4를 출력하고,
5-3을 입력하면 2를 출력합니다.

여러분이 좋아하는 언어와 기술을 이용해서 먼저 해결해 보세요. 하나를 계속 다듬어서 완벽하게 하셔도 좋고,
다양한 언어나 기술을 활용해서 문제를 탐구하셔도 좋습니다.

다음의 과정을 따라서 진행해 주세요:

Q1. 이 프로그램을 사용하는 상황과 사용자를 정합니다.
Q2. 이 프로그램에 무엇을 입력했을 때 어떤 결과가 나올지 여러 가지로 탐구합니다.
Q3. 이 프로그램이 제대로 됐음을 확인할 수 있는 방법을 정합니다.
Q4. 프로그램을 구현합니다.
Q5. 프로그램을 공유합니다.

A1: 계산기를 만들자.
A2: 처음엔 나의 수준을 파악하기 위해 클래스를 이용해 파이썬 콘솔로 사용할 수 있는 프로그램(이하 프로토 타입)을 만들라고 했다.
이후 pyqt를 사용하여 gui도 구성한다. 기능은 숫자 두개를 사칙연산하는 것이다.
pyqt 링크: https://wiki.python.org/moin/PyQt
A3: 프로그램이 제대로 됐는지 확인하기 위해 파이썬 단위 테스크 프레임 워크인 unittest를 사용하라는 필수 사항이 있다.
unittest 링크: https://docs.python.org/ko/3/library/unittest.html
A4: 프로토 타입은 2019-03-08까지 구현, GUI를 구현한 버전은 2019-03-10까지 구현해야한다.
A5: 프로토 타입은 2019-03-09까지 Github에 파일을 올려서 공유하고, GUI를 구현한 버전은 2019-03-11까지 pyinstaller 패키지를 이용해
실행 파일을 만들어서 공유한다.
pyinstaller 링크: https://www.pyinstaller.org/

피드백:
1. while 문이 겹으로 들어가는데, 이걸 최대한 단순하게 만들 수 있을까요?
예를 들어 while 안에 다시 들어오는 while은 반복을 위한 게아니라 그냥 올바른 값을 받기 위해 존재합니다.
그 의미가 드러나도록 함수로 분리할 수 있을까요?
2. FourCalculator는 단순한 동작을 지나치게 많이 추상화한 것 같습니다. 반면 while문 부분은 지나치게 복잡합니다.
어떻게 해야 이 부분을 균형 있게 만들 수 있을까요?
"""
import unittest


class FourCalculator:
    first = 0
    second = 0
    arithmetic_operator = ""
    result = 0
    message = ""
    history = list()
    expression = ""

    def __init__(self):
        print("숫자 2개를 입력하고 연산자 +, -, *, %를 입력합니다.")
        print("계산기를 시작합니다.")

    def __del__(self):
        print("계산기를 종료합니다.\n------------------------\n계산식은 다음과 같습니다.")
        for calculate_history in self.history:
            print(calculate_history)
        print("------------------------")
        input("계산기 이용 내역을 복사하세요. 창을 닫으려면 엔터키를 입력하세요 :)")

    def set_first_value_from_input(self):
        first_user_value = input("숫자를 입력하거나 종료를 원하면 exit를 입력하세요.:")
        if first_user_value == 'EXIT' or first_user_value == 'exit':
            return 1
        try:
            first_user_value = float(first_user_value)
            if first_user_value * 10 == int(first_user_value) * 10:
                self.first = int(first_user_value)
            return 0
        except ValueError as e:
            print("올바른 숫자를 입력하세요.")
            return "ERROR"

    def set_second_value_from_input(self):
        try:
            second_user_value = input("숫자 입력:")
            second_user_value = float(second_user_value)
            if second_user_value*10 == int(second_user_value) * 10:
                self.second = int(second_user_value)
        except ValueError as e:
            print("올바른 숫자를 입력하세요.")
            self.set_second_value_from_input()

    def set_arithmetic_operator(self):
        operator_user_value = input("연산자 입력:")
        if operator_user_value in ['+', '-', '*', '%']:
            self.arithmetic_operator = operator_user_value
            return 1
        print("올바른 연산자를 입력하세요. (+, -, *, %)")
        self.set_arithmetic_operator()

    def add(self):
        self.result = self.first + self.second
        return self.result

    def subtract(self):
        self.result = self.first - self.second
        return self.result

    def multiply(self):
        self.result = self.first * self.second
        return self.result

    def divide(self):
        try:
            self.result = self.first // self.second
            if self.first % self.second:
                self.result = self.first / self.second
        except ZeroDivisionError:
            self.result = "0으로 나눌 수 없습니다."
        return self.result

    def calculate(self):
        if self.arithmetic_operator == '+':
            self.add()
        elif self.arithmetic_operator == '-':
            self.subtract()
        elif self.arithmetic_operator == '*':
            self.multiply()
        elif self.arithmetic_operator == '%':
            self.divide()

        if type(self.result) != str:
            self.expression = str(self.first) + self.arithmetic_operator + str(self.second) + "=" + str(self.result)
            self.history.append(self.expression)
            print(self.history[-1])
            return 1
        print("계산식이 잘못되었습니다.")


class CustomTests(unittest.TestCase):
    def test(self):
        print("숫자 2개를 입력하고 연산자 +, -, *, %를 입력합니다.")
        print("계산기를 시작합니다.")
        cal = FourCalculator()
        while 1:
            while 1:
                try:
                    first_value = input("숫자를 입력하거나 종료를 원하면 exit를 입력하세요.:")
                    if first_value == 'EXIT' or first_value == 'exit':
                        break
                    first_value = int(first_value)
                    cal.set_first_value(first_value)
                    break
                except ValueError as e:
                    print("올바른 숫자를 입력하세요.")
            if first_value == 'EXIT' or first_value == 'exit':
                break

            while 1:
                try:
                    second_value = input("숫자 입력:")
                    second_value = int(second_value)
                    cal.set_second_value(second_value)
                    break
                except ValueError as e:
                    print("올바른 숫자를 입력하세요.")

            while 1:
                arithmetic_operator_value = input("연산자 입력:")
                if arithmetic_operator_value in ['+', '-', '*', '%']:
                    cal.set_arithmetic_operator(arithmetic_operator_value)
                    break
                print("올바른 연산자를 입력하세요. (+, -, *, %)")

            cal.calculate()
            self.assertEqual(cal.get_result(), 4)
            print(cal.get_result())

        print("계산기를 종료합니다.\n------------------------\n계산식은 다음과 같습니다.")
        for i in cal.get_history():
            print(i)
        print("------------------------")


if __name__ == '__main__':
    # unittest.main()
    cal = FourCalculator()
    while 1:
        break_flag = cal.set_first_value_from_input()
        while break_flag == "ERROR":
            break_flag = cal.set_first_value_from_input()
        if break_flag:
            del cal
            break
        cal.set_second_value_from_input()
        cal.set_arithmetic_operator()
        cal.calculate()

"""
숫자 2개를 입력하고 연산자 +, -, *, %를 입력합니다.
계산기를 시작합니다.
숫자 입력를 입력하거나 종료를 원하면 exit를 입력하세요.:3
숫자 입력:3
연산자 입력:+
3+3=6
숫자 입력를 입력하거나 종료를 원하면 exit를 입력하세요.:3
숫자 입력:3
연산자 입력:-
3-3=0
숫자 입력를 입력하거나 종료를 원하면 exit를 입력하세요.:exi
올바른 숫자를 입력하세요.
숫자 입력를 입력하거나 종료를 원하면 exit를 입력하세요.:exi
올바른 숫자를 입력하세요.
숫자 입력를 입력하거나 종료를 원하면 exit를 입력하세요.:exit
숫자 입력:

올바르지 않은 값을 2번 입력하고 exit를 입력했더니 종료되는것을 예상했지만 그렇지 않았다.


    while 1:
        break_flag = cal.set_first_value_from_input()
        while break_flag =="ERROR":
            break_flag = cal.set_first_value_from_input()
        if break_flag:
            del cal
            break
        cal.set_second_value_from_input()
        cal.set_arithmetic_operator()
        cal.calculate()
"""
