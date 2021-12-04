from typing import Text


def decimal_to_big_base(num: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJK"
    result = ''
    while num > 0:
        digit = digits[num % base]
        result += digit
        num = num // base
    return result
if __name__ == '__main__':
    assert(decimal_to_big_base(9, 2) == '1001')
