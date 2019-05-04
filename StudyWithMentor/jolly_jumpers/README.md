# Jolly Jumpers

## 구현할 기능
- n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가 1에서 n-1까지의 값을 모두 가지면
그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다.
- 주어진 수열이 jolly jumper 인지 알려주는 프로그램을 만들기
- 참고 사이트: [코딩도장](http://codingdojang.com/scode/424), [영어로 된 문제 설명](http://users.csc.calpoly.edu/~jdalbey/301/Labs/JollyJumpers.html?fbclid=IwAR2Cq8WMm7xu6XEkhVmwne1XP1HALgQ9vRTcT8t0B_MVUptGu8QlFFrWDfM)

## 구현 방안
- 1부터 n-1까지 수가 담겨 있는 set 자료구조인 변수 set_input을 만든다.
- 문제에서 주어진 n개의 정수가 담겨 있는 배열을 반복문을 돌면서 차를 구한다. 
- 차를 set_input에서 pop한다.
    - 원소가 없어서 pop을 못하는 경우, 졸리점프가 아니므로 Not jolly를 출력한다.