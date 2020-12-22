# 4. Equilibrium Point 
# Given an array A of N positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
def equilibriumPoint(A, N):
    total_sum = sum(A)
    cur_sum = 0
    for i in range(N):
        num = A[i]
        if total_sum - cur_sum - num == cur_sum:
            return i + 1
        cur_sum += num
    return -1