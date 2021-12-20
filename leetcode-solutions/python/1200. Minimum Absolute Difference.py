# https://leetcode.com/problems/minimum-absolute-difference/

import math

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = math.inf
        i = 0
        while i < len(arr) - 1:
            abs_diff = abs(arr[i] - arr[i+1])
            if abs_diff < min_diff:
                ans = [[arr[i], arr[i+1]]]
                min_diff = abs_diff
            elif abs_diff == min_diff:
                ans.append([arr[i], arr[i+1]])
            i += 1
        return ans
