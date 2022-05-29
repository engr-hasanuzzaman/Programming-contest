# https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1/?page=1&difficulty[]=1&status[]=unsolved&company[]=Amazon&sortBy=submissions

class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):
        if not arr:
            return 0

        cur_max = cur_min = arr[0]
        max_product = cur_max

        for i in range(1, n):
            if arr[i] == 0:
                cur_max = float('-inf')
                cur_min = float('inf')
                continue

            if cur_max == float('-inf'):
                cur_max = arr[i]
                cur_min = arr[i]
            else:
                temp = max(cur_max * arr[i], cur_min * arr[i], arr[i])
                cur_min = min(cur_max * arr[i], cur_min * arr[i], arr[i])
                cur_max = temp
            max_product = max(max_product, cur_max, cur_min)
        return max_product


# simplified conditions
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):

        # Variables to store maximum and
        # minimum product till ith index.
        minVal = arr[0]
        maxVal = arr[0]

        maxProduct = arr[0]

        for i in range(1, n, 1):

            # When multiplied by -ve number,
            # maxVal becomes minVal
            # and minVal becomes maxVal.
            if (arr[i] < 0):
                temp = maxVal
                maxVal = minVal
                minVal = temp

            # maxVal and minVal stores the
            # product of subarray ending at arr[i].
            maxVal = max(arr[i], maxVal * arr[i])
            minVal = min(arr[i], minVal * arr[i])

            # Max Product of array.
            maxProduct = max(maxProduct, maxVal)

        # Return maximum product
        # found in array.
        return maxProduct
