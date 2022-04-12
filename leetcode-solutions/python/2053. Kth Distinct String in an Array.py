# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        for s in arr:
            freq[s] += 1
        for s in arr:
            if freq[s] == 1:
                k -= 1
            
            if k == 0:
                return s
        return ""
