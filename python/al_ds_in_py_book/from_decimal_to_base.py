# any number with base, where base <= 10, convert to base 10

def decimal_to_base(num: int, base: int) -> int:
    multiplier, result = 1, 0

    while num > 0:
        result += (num % base) * multiplier
        multiplier *= 10
        num //= base
    return result

print(decimal_to_base(9, 2))