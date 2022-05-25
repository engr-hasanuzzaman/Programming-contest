'''
Consider an array A[] of integers and following two types of queries.

update(l, r, x) : Adds x to all values from A[l] to A[r] (both inclusive).
printArray() : Prints the current modified array.
Input : A [] { 10, 5, 20, 40 }
        update(0, 1, 10)
        printArray()
        update(1, 3, 20)
        update(2, 2, 30)
        printArray()
Output : 20 15 20 40
         20 35 70 60
'''

def diffArray(arr):
    dArray = [0 for _ in range(len(arr) + 1)]
    dArray[0] = arr[0]
    # dArray[i] = arr[i] - arr[i-1]
    for i in range(1, len(arr)):
        dArray[i] = arr[i] - arr[i-1]
    return dArray

def update(dArr, l, r, x):
    dArr[l] += x
    dArr[r+1] -= x

def printArray(arr, dArr):
    ans = []
    for i in range(len(arr)):
        if i == 0:
            arr[i] = dArr[i]
        else:
            arr[i] = arr[i-1] + dArr[i]
    return arr

A = [ 10, 5, 20, 40 ] 
print("input", A)
dArr = diffArray(A)
print(dArr)
update(dArr, 0, 1, 10)
print(printArray(A, dArr))
update(dArr, 1, 3, 20) 
update(dArr, 2, 2, 30) 
print(printArray(A, dArr))
