class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.inc_stack = []

    def push(self, x: int) -> None:
        # max size reached
        if len(self.stack) == self.max_size:
            return
        
        self.stack.append(x)
        self.inc_stack.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        increment_val = self.inc_stack[-1]
        final_val = self.stack.pop() + self.inc_stack.pop()
        
        if len(self.stack) >= 1:
            self.inc_stack[-1] += increment_val
        return final_val

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0: return

        i = min(k, len(self.stack)) - 1
        self.inc_stack[i] += val
