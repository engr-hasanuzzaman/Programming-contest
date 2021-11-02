# https://cp-algorithms.com/algebra/binary-exp.html

# recursive implement
def pow(a: int, b: int) -> int:
    if b == 0:
        return 1
    
    sub_pow = pow(a, b // 2)
    if b % 2 == 1:
        return sub_pow * sub_pow * a
    
    return sub_pow * sub_pow

# test
print('with input 2, 4 ', pow(2, 4) == 16)
print('with input 2, 3 ', pow(2, 3) == 8)
print('with input 2, 5 ', pow(2, 5) == 32)
print('with input 3, 8 ', pow(3, 13) == 1594323)