# partitioner that will partition the array into 3 parts
# on the left lower number than partitioner element
# on the right side larger number than partioner element
# partition index, pivot element
# right element is considered as the pivot element
def partitioner(arr, l, r):
    pivot_element = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot_element:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

arr = [12,3,6,74,23,7,10]
pivot_index = partitioner(arr, 0, len(arr)-1)
print(arr, pivot_index)


