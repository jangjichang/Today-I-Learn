# for문

## 1. 전형적인 for 문
```python
>>> test_list = ['one', 'two', 'three']
>>> for i in test_list:
	print(i)

one
two
three
```

## 2. 다양한 for문의 사용
```python
>>> a = [(1, 2), (3, 4), (5, 6)]
>>> for (first, last) in a:
	print(first + last)
	
3
7
11
```

## 3. for문의 응용
```python
>>> marks = [90, 25, 67, 45, 80]
>>> for i in marks:
	if i > 60:
		print("합격")
	else:
		print("불합격")

		
합격
불합격
합격
불합격
합격
```

## for문과 range함수
```python
>>> a = range(0,10)
>>> for i in a:
	print(i)

	
0
1
2
3
4
5
6
7
8
9
```
- range(시작 숫자, 끝 숫자)에서 시작 숫자는 포함, 끝 숫자는 포함하지 않는다.

## 구구단
```python
>>> for i in range(2,10):
	for j in range(1, 10):
		print(i*j, end=" ")
	print()

	
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36 
5 10 15 20 25 30 35 40 45 
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81 
```

## 리스트 안에 for문 포함하기
```python
>>> a = [1, 2, 3, 4]
>>> result = [num * 3 for num in a]
>>> result
[3, 6, 9, 12]
```
- 리스트안에서 for문 포함하기

```python
>>> a
[1, 2, 3, 4]
>>> result = [num * 3 for num in a if num % 2 == 0]
>>> result
[6, 12]
```
- 리스트안에서 for문, if문 포함하기

```python
[표현식 for 항목 in 반복가능객체 if 조건문]
# 이차원 리스트 생성
m = [[0 for i in range(5)] for j in range(5)]
m = [[0]*5 for i in range(5)]


```

