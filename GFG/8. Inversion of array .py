'''
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Since, we have to complete in O(nlgn), I am using merge sort and counting how many swap needed to sort
'''
#User function Template for python3
import math

# arr[]: Input Array
# N : Size of the Array arr[]
MAX_INPUT_SIZE = 10**18 + 1
def merger(arr, p, q, r):
    swap_count = 0
    left_array = arr[p:q+1]
    right_array = arr[q+1:r+1]
    left_array.append(MAX_INPUT_SIZE)
    right_array.append(MAX_INPUT_SIZE)
    i = 0
    j = 0
    for index in range(p, r+1):
        if left_array[i] > right_array[j]:
            arr[index] = right_array[j]
            j += 1
            swap_count += q-p-i+1 # + 1 for making zero based to 1 based 
        else:
            arr[index] = left_array[i]
            i += 1
    return swap_count

def merge_sort(arr, p, r):
    if p == r:
        return 0

    q = (p+r)//2
    l_count = merge_sort(arr, p, q)
    r_count = merge_sort(arr, q+1, r)
    m_count = merger(arr, p, q, r)
    return l_count + r_count + m_count

def inversionCount(a,n):
    return merge_sort(a, 0, n-1)
