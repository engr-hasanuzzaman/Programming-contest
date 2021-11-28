'''
any base < 10, convert to decimal base
'''

def to_decimal(number, base: int) -> int:
    multiplier, result = 1, 0

    while number > 0:
        result += (number % 10) * multiplier
        multiplier *= base
        number //= 10
    return result

if __name__ == '__main__':
    assert(to_decimal(100, 2) == 4)
    assert(to_decimal(11, 2) == 3)
    assert(to_decimal(1001, 2) == 9)