class MinStack:
    def __init__(self):
        self.minstack = list()
    
    def push(self, x:int) -> None:
        self.minstack.append(x)
    
    def pop(self) -> None:
        self.minstack.pop()
    
    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return min(self.minstack)


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()   # --> Returns -3.
    minStack.pop()
    minStack.top()      # --> Returns 0.
    minStack.getMin()   # --> Returns -2.
