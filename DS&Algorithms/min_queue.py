# min queue that will give the minimum value on a particular time
# the issue with the min queue is that, we will not keep all the value, but only 
# value that will help use determine the min value
from collections import deque

class MinQueue:
    def __init__(self, n):
        self.elm_q = deque([])
        self.min_q = deque([])
        self.size = n
    
    def push(self, elm):
        if self.isFull():
            return
        
        self.elm_q.appendleft(elm)
        position = len(self.elm_q) - 1

        # remove all the larger element as we only want to track the min val
        while self.min_q and self.min_q[0][0] >= elm:
            self.min_q.popleft()
        self.min_q.appendleft((elm, position))

    def isFull(self):
        return len(self.elm_q) == self.size - 1 
    
    def isEmpty(self):
        if not self.elm_q:
            return True
        return False
    
    def pop(self):
        if self.isEmpty():
            return
        
        # handle index of the current min element
        if self.min_q[-1][1] == 0:
            self.min_q.pop()
        else:
            self.min_q[-1] = (self.min_q[-1][0], self.min_q[-1][1] - 1)
        
        self.elm_q.pop()
    
    def min(self):
        if self.isEmpty():
            return None
        return self.min_q[-1][0]
        

# test ing
q = MinQueue(10)
q.push(4)
q.push(1)
print(q.elm_q, q.min()) # this should 1
assert(q.min() == 1)
q.pop()
assert(q.min() == 1)
print(q.elm_q, q.min())
q.pop()
assert(q.min() == None)
print(q.elm_q, q.min())
q.push(10)
q.push(11)
q.push(2)
q.push(12)
q.push(13)
q.push(1)
q.push(14)
q.push(15)
assert(q.min() == 1)
q.pop()
assert(q.min() == 1)
q.pop()
assert(q.min() == 1)
q.pop()
q.pop()
q.pop()
q.pop()
print(q.elm_q)
assert(q.min() == 14)