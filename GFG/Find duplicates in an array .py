# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/0/#

from collections import Counter


class Solution:
    def duplicates(self, arr, n):
        # code here
        ans = []
        frequency = Counter(arr)
        for num, freq in frequency.items():
            if freq > 1:
                ans.append(num)
        return sorted(ans) or [-1]
