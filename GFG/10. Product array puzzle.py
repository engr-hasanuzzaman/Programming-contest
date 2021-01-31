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

'''
2nd way could be creat prefixPro, suffixPro to contain prefix and suffix produc 
that need two extra array
'''

'''
3rd, method using one extra array.
1. Keep profix production on pa array as
    temp = 1
    for i, num in enumberate(arr):
        pa[i] = temp
        temp *= arr[i]
    
2. Traverse array from last to first and update the pa with suffix product
temp = 1
for i in range(n-1, -1, -1):
    pa[i] *= temp
    temp *= arr[i]

so, pa contain the answer
'''

def productExceptSelf(arr, n):
    pa = [1 for _ in range(n)]
    prev_prod = 1
    # update array as a[i] contain left side product
    for i, num in enumerate(arr):
        pa[i] = prev_prod
        prev_prod *= num
        
    # from right to left and update the value with * of right size product
    prev_prod = 1
    for i in range(n - 1, -1, -1):
        pa[i] *= prev_prod
        prev_prod *= arr[i]
    return pa
