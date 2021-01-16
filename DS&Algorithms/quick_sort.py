# partitioner that will partition the array into 3 parts
# on the left lower number than partitioner element
# on the right side larger number than partioner element
# partition index, pivot element
# right element is considered as the pivot element
# N.B: we are partitioning element depending on the partition element
def partitioner(arr, l, r):
    pivot_element = arr[r]
    print("pivot element is ", pivot_element)
    i = l
    for j in range(l, r):
        if arr[j] <= pivot_element:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

arr = [12,3,6,74,23,7,10,3,22,19]
pivot_index = partitioner(arr, 0, len(arr)-1)
print("1st way", arr, pivot_index)

# patitioning using hoars method where pivot is [l+r]/2
def partitioner2(arr, l, r):
    pivot_index = (l+r)//2
    pivot_value = arr[pivot_index]
    print("pivot element is ", pivot_value)
    i = l
    j = r
    while True:
        # on the left side find element that is larget then pivot_element
        # that should have on the right side
        while arr[i] < pivot_value:
            i += 1
        
        # on the right side find element that is smaller then pivot_element
        # that should have on the left side
        while arr[j] > pivot_value:
            j -= 1

        # check wheather all element ar correct postion
        if i >= j:
            return j
        # swap element from both side
        arr[i], arr[j] = arr[j], arr[i]
arr1 = [12,3,6,74,23,7,10,3,22,19]
pivot_index = partitioner2(arr1, 0, len(arr1)-1)
print("2nd way", arr1, pivot_index)