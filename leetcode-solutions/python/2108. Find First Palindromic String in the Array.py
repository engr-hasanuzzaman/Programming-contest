# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if len(words) == 0: return ""
        
        return self.isPalindrom(words[0]) or self.firstPalindrome(words[1:])
    def isPalindrom(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]: return None
            i += 1
            j -= 1
        return s
