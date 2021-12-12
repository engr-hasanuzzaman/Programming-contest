def candies(n, arr):
    c = [None] * n
    i = 0
    while i < n:
        index_cover = update_till_lowest(arr, i, n, c)
        if i != 0:
            # handle edge case
            c[i] = max(c[i], c[i-1] + 1)
        i = index_cover + 1
    return sum(c)
        
def update_till_lowest(arr, i, n, c):
    # base case
    max_i = i
    # increate untill lessthen or equal point
    while max_i < n - 1 and arr[max_i] >= arr[max_i+1]:
        max_i += 1
    
    c[max_i] = 1
    for j in range(max_i - 1, i - 1, -1):
        if arr[j] == arr[j+1]:
            c[j] = 1
        else:
            c[j] = c[j+1] + 1
    return max_i