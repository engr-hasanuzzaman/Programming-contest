# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from itertools import accumulate

class Solution:
    def minOperations(self, nums, x) :
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        remaining_sum = cumsum[-1] - x
        ans = -float("inf")

        # target was > then total sum
        if remaining_sum < 0: return -1
        
        for num in dic:
            # this means if we substrack after num till num + remaining_sum get x
            if num + remaining_sum in dic:
                ans = max(ans, dic[num + remaining_sum] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1