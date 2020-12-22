# Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.
# tips: consider 0 as -1 then create cumulative sum. if sum is 0 then first to this point contain
# same length 0 and 1, betwee number to same numbe also sum to zero
def maxLen(arr, N):
    dict = {}
    cur_sum = 0
    max_size = 0
    for i in range(N):
        num = 1 if arr[i] == 1 else -1
        cur_sum += num
        if cur_sum == 0:
            if i + 1 > max_size:
                max_size = i + 1
        if cur_sum in dict:
            length = i - dict[cur_sum]
            if length > max_size:
                max_size = length
        else:
            dict[cur_sum] = i
    return max_size