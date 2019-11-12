class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def isEmpty(self):
        if self.stack:
            return False
        return True

    def peek(self):
        if self.stack:
            return self.stack[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.peek())
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
