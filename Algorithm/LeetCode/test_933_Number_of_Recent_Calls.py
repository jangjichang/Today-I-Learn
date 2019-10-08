"""
단순히 list를 deque로 바꾸기만해도 속도가 향상된다!
"""


from collections import deque


class RecentCounter:
    def __init__(self):
        self.obj = deque()
        

    def ping(self, t: int) -> int:
        if t:
            self.obj.append(t)
            while True:
                if self.obj[0] < t-3000:
                    self.obj.popleft()
                else:
                    return len(self.obj)
        else:
            return 'null'


if __name__ == "__main__":

    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))