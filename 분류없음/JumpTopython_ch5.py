#연습문제 1

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
#
# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
#
# print(cal.value)  # 10에서 7을 뺀 3을 출력


#연습문제 2

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
# add method를 오버라이딩했음
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value >= 100:
#             self.value = 100
#
#
# cal = MaxLimitCalculator()
# cal.add(50)  # 50 더하기
# cal.add(60)  # 60 더하기
#
# print(cal.value)  # 100 출력

# 5-2 모듈
# 모듈이란 함수나 변수 또는 클래스들을 모아 놓은 파일이다.

# 5-3 패키지

"""
패키지는 도트(.)를 이용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해준다.
예를 들어 모듈명이 A.B인 경우 A는 패키지명이 되고 B는 A패키지의 B모듈이 된다.

가상의 game 패키지 예
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

game, sound, graphic, play는 디렉터리명이고, .py 확장자를 가진 파일은 파이썬 모듈이다.
game 디렉터리가 이 패키지의 루트 디렉터리이고 sound, graphic, play는 서브 디렉터리이다.

__init__.py의 용도

해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
만약 game, sound, graphic등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.
"""

"""
5-4 예외 처리

try, except문

try:
    ...
except: [발생오류[as 오류 메시지 변수]]:
    ...
"""

# f = open("doesnotexist", 'r')

# a = 4/0

# b = [1, 2, 3]
# b[4]

"""
# 오류를 발생시키는 예제
# Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현해야한다.
class Bird:
    def fly(self):
        raise NotImplementedError


# class Eagle(Bird):
#     pass
#
#
# eagle = Eagle()
# eagle.fly()


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
"""


# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)
#
#
# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않은 별명입니다."
#
#
# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)


# 5-4 연습문제 1번

# result = 0
# try:
#     [1, 2, 3][3]
#     "a"+1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4
#
# print(result)


# 5-5 내장함수
# 파이썬 내장 함수들은 외부 모듈과는 달리 import를 필요로 하지 않는다.
# 아무런 설정 없이 바로 사용할 수 있다.

# eval은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴한다.
print(eval('1+2+3'))

a = [3, 1, 2]

# sorted함수는 입력 값을 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
# 리스트 자료형에도 sort라는 함수가 있지만, 그것은 객체 자체를 정렬하고 결과를 리턴하지 않는다.
print("sorted(a)")
sorted(a)
print("a: ")
print(a)
print("a.sort(): ")
a.sort()
print("a: ")
print(a)


# 5-6 외장함수
# 파이썬 사용자들이 만든 유용한 프로그램들을 모아 놓은 것이 바로 파이썬 라이브러리이다.
# 파이썬 라이브러리는 파이썬 설치 시 자동으로 컴퓨터에 설치가 된다.


