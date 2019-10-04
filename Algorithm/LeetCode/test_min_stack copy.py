"""
getmin 메소드의 수행 시간을 o(1)로 줄였습니다.
"""
class MinStack:
    def __init__(self):
        self.minstack = list()
        self.min = list()
    
    def push(self, x:int) -> None:
        self.minstack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            if self.min[-1] >= x:
                self.min.append(x)
    
    def pop(self) -> None:
        pop_ele = self.minstack.pop()
        if pop_ele == self.min[-1]:
            self.min.pop()
        
    
    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()   # --> Returns -3.
    minStack.pop()
    minStack.top()      # --> Returns 0.
    minStack.getMin()   # --> Returns -2.
