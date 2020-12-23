# Given an unsorted array A of size N of non-negative integers, 
# find a continuous sub-array which adds to a given number S.
def sub_array(arr, sum):
    cur_sum = 0
    left = 0
    for i in range(len(arr)): # 1 2 3 7 5
        num = arr[i]
        cur_sum += num
        
        if cur_sum == sum:
            return (left+1, i+1)
        elif cur_sum > sum:
            while cur_sum > sum and left < i:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == sum:
                return (left+1, i+1)
            
    return -1
# input section
T = int(input())
for _ in range(T):
    N, S = [int(num) for num in input().split(" ")]
    arr = [int(num) for num in input().split(" ")[:N]]
    ans = sub_array(arr, S)
    if ans == -1:
        print(-1)
    else:
        print("{} {}".format(ans[0], ans[1]))