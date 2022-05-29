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
