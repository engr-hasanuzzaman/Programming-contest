'''
Given an array arr[] of N positive integers and a number K. 
The task is to find the kth smallest element in the array.
Solution: sort the array and return 
'''
def kthSmallest(a,n,k):
    a.sort()
    return a[k-1]