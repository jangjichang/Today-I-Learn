# 파일 읽고 쓰기


# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


# readline() 함수 이용하기
# 가장 첫 번째 줄이 출력됩니다.


# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()


# 모든 라인을 읽어서 화면에 출력하기 (readline() 사용)


# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()


# 모든 라인을 읽어서 화면에 출력하기 (readlines() 사용)

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()


# 모든 라인을 읽어서 화면에 출력하기 (read() 사용)

# f = open("새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()


# 파일에 새로운 내용 추가하기

# f = open("새파일.txt", 'a+')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
#
# data = f.read()
# print(data)
# f.close()


# with 문 사용하기 이것을 사용하면 파일을 닫을 때 close()를 하지 않아도 된다.
# with는 python 2.5부터 지원됨

# with를 사용하지 않은 경우

# f = open('foo.txt', 'w')
# f.write("Life is too short, you need python")
# f.close()


# with를 사용한 경우

# with open('foo.txt', 'w') as f:
#     f.write("Life is too short, you need python")

import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)

# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')


# 연습문제 1번

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
#
# f2 = open('test.txt', 'r')
# print(f2.read())
# f2.close()


# 연습문제 2번

# data = input('저장할 내용을 입력하세요:')
# f1 = open("test.txt", 'a')
# f1.write(data)
# f1.write('\n')
# f1.close()


# 연습문제 3번
# 파일을 열어서 읽고 내용을 지우고 역순으로 쓰기를 한다.

# with open('abc.txt', 'r') as f:
#     data = f.readlines()
#
# data.reverse()
#
# with open('abc.txt', 'w') as f:
#     for line in data:
#         line = line.strip()
#         f.write(line)
#         f.write('\n')


# 연습문제 4번

# with open('test.txt', 'r') as f:
#     data = f.read()
#
# data = data.replace('java', 'python')
#
# with open('test.txt', 'w') as f:
#     f.write(data)


# 연습문제 5번

sum = 0
avg = 0

with open('sample.txt', 'r') as f:
    data = f.readlines()
    for i in data:
        sum += int(i)
    avg = sum/len(data)

with open('result.txt', 'w') as f:
    f.write('총합: %d\n' % sum)
    f.write('평균: %f' % avg)
