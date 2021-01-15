# time complexity O(n*2)
# time limit exceed
def longestSubsequence(a,n):
    # code here
    # return length of the longest increasing sub sequence
    dp = [0] * n
    max_size = 0
    for i in range(n-1, -1, -1):
        c_max = -1
        j = i+1
        while j < n:
            if a[j] > a[i]:
                c_max = max(dp[j], c_max)
            j += 1
        if c_max != -1:
            dp[i] = c_max + 1 
            
        if c_max + 1 > max_size:
            max_size = c_max + 1
    return max_size + 1