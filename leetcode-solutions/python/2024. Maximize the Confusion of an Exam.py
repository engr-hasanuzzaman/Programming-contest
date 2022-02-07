# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maxSize('T', answerKey, k), self.maxSize('F', answerKey, k))
        
    def maxSize(self, oChar, answerKey, conTimes):
        left = right = 0
        max_size = 0
        while right < len(answerKey):
            char = answerKey[right]
            if char == oChar:
                conTimes -= 1
            # need to shrink the window size
            if conTimes < 0:
                while conTimes < 0:
                    if answerKey[left] == oChar:
                        conTimes += 1
                    left += 1
            max_size = max(max_size, right - left + 1)
            right += 1
        return max_size
