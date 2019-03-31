# https://www.python-course.eu/python3_inheritance_example.php
# 클래스 공부하기!

class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(C, B):
    # pass
    def m(self):
        B.m(self)


x = D()
print(x.m())
