# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = "0123456789abcdef"
        result = ''
        # num + 2's complement of number == 2 ** N where N is number of bit of that number
        # so 2's complement = 2 ** N - num ->
        if num < 0:
            num += 2 ** 32
        while num > 0:
            digit = digits[num % 16]
            result = digit + result
            num //= 16
        return result
