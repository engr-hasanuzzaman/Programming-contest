# Given an array of size N containing only 0s, 1s, and 2s; 
# sort the array in ascending order.
# since the number of elemen is small, use count sort
def sort012(arr,n):
    zero_count = 0
    one_count = 0
    two_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num == 1:
            one_count += 1
        else:
            two_count += 1
    i = 0
    for _ in range(zero_count):
        arr[i] = 0
        i += 1
    for _ in range(one_count):
        arr[i] = 1
        i += 1
        
    for _ in range(two_count):
        arr[i] = 2
        i += 1