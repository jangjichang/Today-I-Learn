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

