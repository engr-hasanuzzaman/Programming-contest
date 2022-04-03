# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        size = len(words)
        word_int = [0] * size
        for k, word in enumerate(words):
            int_value = 0
            for i in range(len(word)):
                int_value |= (1 << (ord(word[i]) - ord('a')))
            word_int[k] = int_value

        ans = 0
        for i in range(size - 1):
            for j in range(i+1, size):
                if (word_int[i] & word_int[j]) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
