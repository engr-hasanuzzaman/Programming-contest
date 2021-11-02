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

def powItaretive(a: int, b: int)->int:
    res = 1
    while b != 0:
        if b % 2:
            res = res * a
        # every time it will be double
        a = a * a
        b = b >> 1
    return res

    # test
print('with input 2, 4 ', powItaretive(2, 4) == 16)
print('with input 2, 3 ', powItaretive(2, 3) == 8)
print('with input 2, 5 ', powItaretive(2, 5) == 32)
print('with input 3, 8 ', powItaretive(3, 13) == 1594323)