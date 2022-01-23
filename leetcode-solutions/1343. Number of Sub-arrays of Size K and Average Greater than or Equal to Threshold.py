# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_total = sum(arr[:k])
        ans = 0
        for i in range(k, len(arr)):
            if (current_total // k) >= threshold:
                ans += 1
            current_total -= arr[i-k] # remove tha last number
            current_total += arr[i]

        if (current_total // k) >= threshold:
                ans += 1 
            
        return ans
