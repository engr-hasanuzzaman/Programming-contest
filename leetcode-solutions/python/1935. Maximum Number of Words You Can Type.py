# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenKeys = {}
        for _, c in enumerate(brokenLetters):
            brokenKeys[c] = True
        words = text.split(" ")
        ans = len(words)
        for _, word in enumerate(words):
            for _, c in enumerate(word):
                if c in brokenKeys:
                    ans -= 1
                    break
        return ans
