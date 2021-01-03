import sys

def findMin(a, n):
     
    su = 0
     
    # Calculate sum of all elements 
    su = sum(a)
    print(su)
    # Create an 2d list to store 
    # results of subproblems
    dp = [[0 for i in range(su + 1)] 
             for j in range(n + 1)]
 
    # Initialize first column as true.
    # 0 sum is possible 
    # with all elements. 
    for i in range(n + 1):
        dp[i][0] = True
         
    # Initialize top row, except dp[0][0],
    # as false. With 0 elements, no other 
    # sum except 0 is possible
    for j in range(1, su + 1):
        dp[0][j] = False
     
    # Fill the partition table in 
    # bottom up manner
    for i in range(1, n + 1):
        for j in range(1, su + 1):
             
            # If i'th element is excluded 
            dp[i][j] = dp[i - 1][j]
             
            # If i'th element is included
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
     
    # Initialize difference 
    # of two sums.
    diff = sys.maxsize
 
    # Find the largest j such that dp[n][j] 
    # is true where j loops from sum/2 t0 0 
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
             
    return diff
arr = [8, 529, 382, 130, 462, 223, 167, 235, 529]
print(findMin(arr, len(arr)))