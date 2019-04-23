# self number 문제에 TDD 적용하기

- [Self Number 문제 풀이](https://www.youtube.com/watch?v=YN-vapyv_dg)를 보고 TDD에 대해 알아보았다.
- python에 unittest 라이브러리가 있지만, pytest, pytest-watch를 설치하여 tdd를 진행한다.

- 테스트를 진행할 때 함수명, 파일명앞에 test_를 붙여줘야한다.
>> 정확히 test_를 붙여야하는지는 모르겠지만, test_를 붙이지 않으면 pytest가 인식하지 못하는 듯하다.

```python
import unittest


class SelfNumberTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, 1+1)


if __name__ == '__main__':
    unittest.main()
```
- 코드를 작성하고 커맨드창에서 pytest를 입력하면 결과가 출력된다.
```buildoutcfg
========================== test session starts ==========================
platform win32 -- Python 3.6.6, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: C:\Users\jc\Documents\GitHub\Today-I-Learn\StudyWithMentor\selfnu
mber, inifile:
collected 1 item                                                         

test_self_number.py F                                              [100%]

=============================== FAILURES ================================
______________________ SelfNumberTest.test_sample _______________________

self = <test_self_number.SelfNumberTest testMethod=test_sample>

    def test_sample(self):
>       self.assertEqual(1, 1+1)
E       AssertionError: 1 != 2

test_self_number.py:6: AssertionError
======================= 1 failed in 0.08 seconds ========================

```
- 하지만 이런식으로 코드수정하고 명령어치는 작업을 반복하지 않고 pytest-watch를 이용하면 실시간으로 반영할 수 있다.

- pytest-watch 명령어를 치면 실시간으로 test를 진행해준다.