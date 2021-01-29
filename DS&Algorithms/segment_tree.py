# Main concent: divide array into two sub-array, keep lower part as left child, higher part as right child
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

# ex. 4 -> 4, 5/6/7 -> 8 ...
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
# arr = [-1, 0, 3, 6]
segmentTree = [float('inf')] * (2 * nearestLargePowerOf2(len(arr)) - 1)
constructSegmentTree(arr, segmentTree, 0, len(arr) - 1, 0)
print(segmentTree)

# range query
# low, high indicate original range that we have kept 
# so, pos kept the min value of range [low, high] kept min value of is the marking range
# qlow, qhigh our search range
def rangeQuery(segmentTree, qlow, qhigh, low, high, pos):
    # print("------", low, high, pos)
    # complete overlap
    if qlow <= low and qhigh >= high:
        return segmentTree[pos]
    
    # no overlap
    if qhigh < low or qlow > high:
        return float('inf')
    
    # partial overlap
    # alway divide current arr into two sub array where
    # low to mid is left child, mid + 2 to high right child
    mid = (low + high) // 2
    leftVal = rangeQuery(segmentTree, qlow, qhigh, low, mid, pos*2 + 1) 
    rightVal = rangeQuery(segmentTree, qlow, qhigh, mid + 1, high, pos*2 + 2) 
    return min(leftVal, rightVal)

assert(rangeQuery(segmentTree, 1, 5, 0, 5, 0) == 0)
assert(rangeQuery(segmentTree, 0, 2, 0, 5, 0) == -1)
assert(rangeQuery(segmentTree, 1, 2, 0, 5, 0) == 3)
assert(rangeQuery(segmentTree, 0, 5, 0, 5, 0) == -1)