# Django 기초편 1,2장
# python library를 이용해 간단한 서버를 만들기

import urllib.parse
import urllib.request

#  urllib.parse 모듈은 URL의 분해, 조립, 변경 등을 처리하는 함수를 제공
result = urllib.parse.urlparse('http://www.python.org:80/guido/python.html;philosophy?overall=3#n10')
# print(result)

# urllib.request 모듈은 주어진 URL에서 데이터를 가져오는 기본 기능을 제공
f = urllib.request.urlopen("http://www.example.com")
# print(f.read(500).decode('utf-8'))

# post method를 테스트하기 위해 실습 서버를 실행하고 진행함
data = "language=python&framework=django"
f = urllib.request.urlopen('http://127.0.0.1:8000', bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))