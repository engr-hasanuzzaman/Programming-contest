# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        memo = {}
        for i in range(len(sentence)):
            if sentence[i] in memo:
                memo[sentence[i]] += 1
            else:
                memo[sentence[i]] = 1
        for n in range(26):
            c = chr(ord('a') + n)
            if c not in memo:
                return False
        return True

        