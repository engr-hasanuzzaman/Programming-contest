def push(arr, ele):
    # Code here
    if isEmpty(arr):
        min_val = ele
    else:
        min_val = min(arr[-1][1], ele)
    arr.append((ele, min_val))

# Function should pop an element from stack
def pop(arr):
    # Code here
    if not isEmpty(arr):
        arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return len(arr) == n-1

# function should return 1/0 or True/False
def isEmpty(arr):
    if not arr:
        return True
    
    return False
    #Code here

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    if not isEmpty(arr):
        return arr[-1][1]
