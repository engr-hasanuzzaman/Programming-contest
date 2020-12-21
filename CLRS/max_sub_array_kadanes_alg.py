# max_sub arry of ith position of A is [A[i], max of [A[i], max_sum(A[1..i-1] + A[i]]
def maxSubArraySum(a,size):
    max_sum = -100000000
    sum = 0
    for n in a:
        sum = max([n, n+sum])
        if sum > max_sum:
            max_sum = sum
    return max_sum