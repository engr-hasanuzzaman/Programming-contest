# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        digits = '0123456'
        res = ''
        is_neg = num < 0
        if num < 0:
            num = -num
        while num > 0:
            digit = digits[num%7]
            res = digit + res
            num //= 7
        return "-" + res if is_neg else res
