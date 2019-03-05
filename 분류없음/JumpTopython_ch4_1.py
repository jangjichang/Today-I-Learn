# 함수, 입력과 출력, 파일 처리 방법


'''
매개변수와 인수
매개변수: 함수에 입력으로 전달된 값을 받는 변수
인수: 함수를 호출할 때 전달하는 입력 값 
'''


def add(a, b):  # a, b는 매개변수
    return a+b


# print(add(3, 4))    # 3, 4는 인수


def add1(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


a = add1(3, 4)
print(a)


# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


add_result = add_many(1, 2, 3, 4, 5)
print(add_result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)


result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name='foo', age=3)


def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("장지창", 27)


# 함수 안에서 선언된 변수의 효력 범위
def vartest(a):
    a = a+1
    return a

a = vartest(3)
print(a)


def listtest(a):
    a.append(1)
    result = a[:]
    return result

aa = listtest([1,2,3,4,5])
print(aa)


def is_odd(num):
    return bool(num % 2)


def all_avg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

print('----------')

print(all_avg(1, 2, 3, 4, 5, 6))


# 사용자 입력
a = input()
print(a)

number = input("숫자를 입력하세요: ")

# 한줄에 결과값 출력
for i in range(10):
    print(i, end=' ')


input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다." % total)

input_list = input("숫자를 입력하세요.").split(',')

sum = 0
for i in input_list:
    sum += int(i)

print("입력한 숫자의 총합은 %d입니다." % sum)

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
for i in range(1, 10):
    print(dan*i, end=' ')