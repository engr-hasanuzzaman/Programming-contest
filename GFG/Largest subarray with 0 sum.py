# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/
class Solution:
    def maxLen(self, n, arr):
        prefix_sum = {}
        p_sum = 0
        max_size = 0
        for i in range(n):
            p_sum += arr[i]

            if p_sum == 0:
                max_size = max(max_size, i+1)

            if p_sum in prefix_sum:
                # print("--", i, prefix_sum[p_sum], prefix_sum, p_sum)
                max_size = max(max_size, i - prefix_sum[p_sum])
            else:
                prefix_sum[p_sum] = i
        return max_size
