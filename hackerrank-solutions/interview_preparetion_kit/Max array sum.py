def maxSubsetSum(arr):
    if len(arr) <= 2:
        return max(max(arr), 0) # return zero for neg number
    
    sum_a = [max(arr[0], 0), max(arr[1], arr[0], 0)]
    for i in range(2, len(arr)):
        sum_a.append(max(arr[i] + sum_a[i-2], sum_a[i-1]))
    return max(sum_a)
