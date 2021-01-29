# arr -> input array from where we will construct the segment tree
# segmentArr -> where we will kepp tree as root of i -> (i-1)/2, child of i: 2*i + 1, 2*i+2
# low -> current lower index. Initial val 0
# high -> current higher index, Initial value: arr size - 1
# pos -> postion in segment tree. Initial val 0 as we keep root on 0
def constructSegmentTree(arr, segmentArr, low, hight, pos):
