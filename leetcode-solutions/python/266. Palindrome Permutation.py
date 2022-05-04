# https://leetcode.com/problems/palindrome-permutation/

from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_counter = defaultdict(int)
        for char in s:
            freq_counter[char] += 1
        
        odd_number = 0
        for freq in freq_counter.values():
            if freq % 2 == 1:
                odd_number += 1
                
            if odd_number > 1:
                return False
        return True