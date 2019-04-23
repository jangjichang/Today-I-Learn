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

수정사항:
1. FourCalculator함수에서 set_value, set_first_value, set_second_value, set_arithmetic_operator 함수를
set_first_value, set_second_value, set_arithmetic_operator 함수로 변경하였습니다.
올바른 값을 받는지 확인하는 부분도 이 함수에 추가하여 올바른 값을 받는 의미가 드러나도록 작성하였습니다.

2.
단순한 동작을 지나치게 많이 추상화한 것이 아래 메소드라고 생각하여 코드를 수정했습니다.
에러 메시지를 가져오는 get_error_msg 메소드,
계산 결과를 가져오는 get_result 메소드,
연산 히스토리를 가져오는 get_history 메소드를 삭제했습니다.

다만, 연산 히스토리를 저장하는 set_history 메소드는 calculate 메소드 안에서 호출하여 연산 히스토리를 저장합니다.

while 문 부분이 지나치게 복잡한 것은 1번 사항에서 반영한 것과 중복되는 내용입니다. 올바른 값을 가져오는지 체크하는 기능을 메소드에
추가했습니다.

++ 추가적으로 calculate 메소드에서 연산자에 따라 분기하여 계산하는 부분을 if, else를 사용하지 않고
dictionary형 변수인 'operators'에 연산자 (+, -, *, %)를 key로,
그에 해당되는 함수(add, subtract, multiply, divide)를 value로 설정하였습니다.
"""
import unittest


class FourCalculator:
    first = 0
    second = 0
    arithmetic_operator = ""
    result = 0
    message = ""
    history = list()
    exit_flag = 0

    def __init__(self):
        print("숫자 2개를 입력하고 연산자 +, -, *, %를 입력합니다.")
        print("계산기를 시작합니다.")

    def __del__(self):
        print("계산기를 종료합니다.\n------------------------\n계산식은 다음과 같습니다.")
        for calculate_history in self.history:
            print(calculate_history)
        print("------------------------")
        input("계산기 이용 내역을 복사하세요. 창을 닫으려면 엔터키를 입력하세요 :)")

    def set_first_value(self):
        try:
            first_user_value = input("숫자를 입력하거나 종료를 원하면 exit를 입력하세요.:")
            if first_user_value == 'EXIT' or first_user_value == 'exit':
                self.exit_flag = 1
                return 0

            self.first = float(first_user_value)
            if self.first * 10 == int(self.first) * 10:
                self.first = int(self.first)
                return 1
        except ValueError as e:
            print("올바른 숫자를 입력하세요.")
            self.set_first_value()

    def set_second_value(self):
        try:
            second_user_value = input("숫자 입력:")
            self.second = float(second_user_value)
            if self.second * 10 == int(self.second) * 10:
                self.second = int(self.second)
        except ValueError as e:
            print("올바른 숫자를 입력하세요.")
            self.set_second_value()

    def set_arithmetic_operator(self):
        operator_user_value = input("연산자 입력:")
        if operator_user_value in ['+', '-', '*', '%']:
            self.arithmetic_operator = operator_user_value
            return 1
        print("올바른 연산자를 입력하세요. (+, -, *, %)")
        self.set_arithmetic_operator()

    def set_history(self):
        if type(self.result) != str:
            expression = str(self.first) + self.arithmetic_operator + str(self.second) + "=" + str(self.result)
            self.history.append(expression)
            print(self.history[-1])
            return 1
        print(self.result)

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
        self.operators[self.arithmetic_operator](self)
        self.set_history()

    operators = {'+': add,
                 '-': subtract,
                 '*': multiply,
                 '%': divide
                 }


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
        cal.set_first_value()
        if cal.exit_flag:
            del cal
            break
        cal.set_second_value()
        cal.set_arithmetic_operator()
        cal.calculate()


"""
연산자에 따라 if, else문을 쓰지 않고 dict를 사용해서 연산하도록 수정했음
add, substract등 에서 expression을 history에 저장하는 방법 생각하기
"""
