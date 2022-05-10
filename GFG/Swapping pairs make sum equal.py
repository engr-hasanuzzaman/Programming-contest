# https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:
    def findSwapValues(self, a, n, b, m):
        sum_a = sum(a)
        sum_b = sum(b)

        if (sum_a + sum_b) % 2 == 1:
            return -1

        # ensure sum_a is greater
        if sum_b > sum_a:
            sum_b, sum_a = sum_a, sum_b
            a, b = b, a

        diff = (sum_a - sum_b) // 2

        nums = set(b)
        for num in a:
            if (num - diff) in nums:
                return 1
        return -1
