# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        digit_sum = 0
        while num > 9:
            digit_sum += (num // 10)
            num %= 10
        return self.addDigits(digit_sum + num)
