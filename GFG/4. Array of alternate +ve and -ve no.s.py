'''
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
'''

# solve the problem with queue
# keep position number to one queue and negetive to other
# replace arr number from the queue depending on i % 2 value
from collections import deque

class Solution:
    def rearrange(self,arr, n):
        pQueue = deque([])
        nQueue = deque([])
        for num in arr:
            if num < 0:
                nQueue.appendleft(num)
            else:
                pQueue.appendleft(num)
        
        for i in range(n):
            if (i % 2 == 0 and pQueue) or (i % 2 == 1 and not nQueue):
                arr[i] = pQueue.pop()
            elif (i % 2 == 0 and not pQueue) or (i % 2 == 1 and nQueue):
                arr[i] = nQueue.pop()
