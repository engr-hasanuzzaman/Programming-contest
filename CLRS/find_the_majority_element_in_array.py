# find the majority elemen who frequency is > (size / 2)
# if there is no element then return -1
def majorityElement(A,N):
    dict = {}
    if N == 1:
        return A[0]
    
    for num in A:
        if num in dict:
            dict[num] += 1
            if dict[num] > (N // 2):
                return num
        else:
            dict[num] = 1
    return -1