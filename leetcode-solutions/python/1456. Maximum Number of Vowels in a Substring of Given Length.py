# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_number = cur_number = 0
        for i in range(k):
            if s[i] in vowels:
                cur_number += 1
        max_number = cur_number
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cur_number -= 1
            if s[i] in vowels:
                cur_number += 1
            max_number = max(max_number, cur_number)
        return max_number
