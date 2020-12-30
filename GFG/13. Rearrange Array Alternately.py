'''
rearrange  the array elements alternatively i.e first element should be max value, 
second should be min value, third should be second max, fourth should be second min and so on.
'''
def rearrange(arr, n): 
    ans = []
    left = 0
    right = n -1
    while left <= right:
        ans.append(arr[right])
        ans.append(arr[left])
        left += 1
        right -= 1
    if left == right:
        ans.append(arr[left])
    for i in range(n):
        arr[i] = ans[i]
