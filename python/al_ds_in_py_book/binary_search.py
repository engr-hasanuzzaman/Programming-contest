# alternate implementation of binary search

def binary_search(arr, x):
    print('----------', arr, x)
    k = 0
    b = len(arr) // 2
    while b >= 1:
        print('--- top while', b, k)
        while (k + b < len(arr)) and arr[k+b] <= x:
            print('--- inner while', b, k)
            k += b
        b //= 2
    print('output', k)
    if arr[k] == x:
        return k
    return -1

if __name__ == '__main__':
    assert(binary_search([1,2,3,4,5,7,8,9,10], 10) == 8)
    assert(binary_search([1,2,3,4,5,7,8,9,10], 6) == -1)
    assert(binary_search([1,2,3,4,5,7,8,9,10], 19) == -1)