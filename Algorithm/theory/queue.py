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
