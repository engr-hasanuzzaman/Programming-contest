# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def push(self, x: int) -> None:
        self.enqueueStack.append(x)

    def pop(self) -> int:
        if not self.dequeueStack:
            self.transferEntoDeQueue()

        if not self.dequeueStack:
            return -1
        return self.dequeueStack.pop()
            

    def peek(self) -> int:
        if not self.dequeueStack:
            self.transferEntoDeQueue()

        return self.dequeueStack[-1]

    def empty(self) -> bool:
        return not(self.enqueueStack or self.dequeueStack)
    
    def transferEntoDeQueue(self):
        while self.enqueueStack:
            self.dequeueStack.append(self.enqueueStack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()