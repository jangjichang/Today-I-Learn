# 알고리즘 스터디 1주차 스택, 큐

# Intro

Oct 15, 2019 장지창

안녕하세요. 프로그라피 5기 Django팀 장지창입니다.

오늘은 알고리즘 스터디 1주차에 진행한 스택, 큐에 대해 알아보겠습니다. 저희는 매주 두개의 자료구조 주제를 선정하여 관련 문제를 풉니다. 그리고 오프라인에서 개념 강의를 제공하는 방식으로 스터디가 진행되고 있습니다.

지금부터 아래에서 언급하는 내용은 제가 알고리즘 스터디를 준비하면서 스택, 큐에 대해 알아본 내용입니다. 혹시나 틀린 부분이 있거나 다른 생각이 있으시다면 댓글이나 이메일을 통해 서로 의견을 공유할 수 있으면 좋을 것 같습니다.

---

# 개념 설명

저번 글에 이어서 큐를 소개하겠습니다. 큐는 스택과 반대로 FIFO(First In First Out)순서를 따르는 선형 데이터 구조입니다. 

큐의 삭제 및 삽입은 front end와 rear end에서 수행됩니다. 새로운 요소의 추가는 rear end에서 수행되고 기존 요소의 삭제는 front end에서 수행됩니다.

![queue](queue.jpg)

큐에 어떤 연산이 있는지 알아볼까요?
- enqueue: 큐에 새로운 요소를 추가합니다.
- dequeue: 큐에서 요소를 제거합니다.
- peek: 큐의 맨 위 요소를 반환합니다.
- isEmpty: 큐가 비어있는지 확인합니다.

그렇다면 큐를 어떻게 구현할까요? python tutorial 공식 문서의 [리스트를 큐로 사용하기](https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-queues)를 살펴보겠습니다.

리스트를 큐로 사용하는 것도 가능한데 리스트는 이 목적에는 효율적이지 않습니다. 리스트의 끝에 덧붙이거나, 끝에서 꺼내는 것은 빠르지만, 리스트의 맨앞에 덧붙이거나 맨앞에 꺼내는 것은 느립니다. 왜냐하면 리스트의 맨앞에 붙이거나 꺼낼 때 다른 요소들을 모두 한 칸씩 이동시켜야 하기 때문이죠.

큐를 구현하려면, 양 끝에서의 덧붙이기와 꺼내기가 모두 빠르도록 설계된 `collections.deque`를 사용하는 것이 좋습니다. `enqueue`와 `dequeue`연산은 collections.deque에 설계된 것을 따랐고 `isEmpty`와 `peek`


```python
from collections import deque


class Queue():
    def __init__(self, values=list()):
        self.queue = deque(values)

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if self.queue:
            self.queue.popleft()

    def isEmpty(self):
        if self.queue:
            return False
        return True

    def peek(self):
        if self.queue:
            return self.queue[-1]


if __name__ == "__main__":
    q = Queue(["이동주", "장지창", "한수민"])
    q.enqueue("김건호")
    q.enqueue("김은향")
    q.enqueue("조예지")
    q.dequeue()
    q.dequeue()
    q.peek()
    q.dequeue()
    q.dequeue()
    q.peek()

```

---

# 관련 문제
- https://leetcode.com/problems/number-of-recent-calls/
- https://programmers.co.kr/learn/courses/30/lessons/42587

회고 추가

# 참고
- https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-queues
- https://techdifferences.com/difference-between-stack-and-queue.html