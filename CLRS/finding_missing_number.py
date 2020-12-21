def MissingNumber(array,n):
    expected_number = n * (n + 1) // 2
    given_sum = sum(array)
    return expected_number - given_sum