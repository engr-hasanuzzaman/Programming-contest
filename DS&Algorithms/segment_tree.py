# arr -> input array from where we will construct the segment tree
# segmentArr -> where we will kepp tree as root of i -> (i-1)/2, child of i: 2*i + 1, 2*i+2
# low -> current lower index. Initial val 0
# high -> current higher index, Initial value: arr size - 1
# pos -> postion in segment tree. Initial val 0 as we keep root on 0
def constructSegmentTree(arr, segmentArr, low, high, pos):
    if low == high:
        segmentArr[pos] = arr[low]
        return
    mid = (low + high) // 2
    # left child that is 2*i+1
    constructSegmentTree(arr, segmentArr, low, mid, 2*pos + 1)
    # right child
    constructSegmentTree(arr, segmentArr, mid + 1, high, 2*pos + 2)
    # parent will contain min of it's children
    segmentArr[pos] = min(segmentArr[2*pos + 1], segmentArr[2*pos + 2])

def nearestLargePowerOf2(N):
        if N & (N - 1) == 0:
            return N
        
        while N & (N-1) != 0:
            N = N - (N & -N)
        
        return 2*N

# if the size of input array is n
# n is power of 2 then size of the segment tree will be 2*n - 1 
# otherwise next powere of 2 of n (M) 2*M - 1 size of the segment tree will be 
# ex, for 5,6,7 segmentTree array size will be 8*2 - 1
arr = [-1,3,4,0,2,1]
segmentTree = [float('inf')] * (2 * nearestLargePowerOf2(len(arr)) - 1)
constructSegmentTree(arr, segmentTree, 0, len(arr) - 1, 0)
print(segmentTree)
