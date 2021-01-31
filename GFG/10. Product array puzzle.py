from functools import reduce
'''
main point of this question is to handle the zero value, if there are multiple zero
than all the production will be zero, if there is one zero, except zero value all the
product will be zero and other element will be total product except zero
'''
def productExceptSelf(arr, n):
    total_product = 1
    zeroCount = 0
    pArr = []
    for num in arr:
        if num == 0:
            zeroCount += 1
            continue
        total_product *= num
    
    if zeroCount > 1:
        return [0] * n
    elif zeroCount == 1:
        for num in arr:
            if num == 0:
                pArr.append(total_product)
            else:
                pArr.append(0)
        return pArr
    
    for num in arr:
        pArr.append(total_product // num)
    return pArr