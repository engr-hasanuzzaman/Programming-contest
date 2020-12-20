def maxSubArraySum(a,size):
    ##Your code here
    i = 0
    max_sum = -100000000;
    while i < size:
        j = i;
        sum = 0;
        while j < size:
            sum += a[j]
            if sum > max_sum:
                max_sum = sum
            j += 1
        i += 1
    return max_sum