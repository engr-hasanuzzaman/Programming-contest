# https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:
    def allPairs(self, A, B, N, M, X):
        set_b = set(B)
        ans = []
        for idx, num in enumerate(A):
            rem = X - num
            if rem in set_b:
                ans.append([num, rem])
        ans.sort()
        return ans
