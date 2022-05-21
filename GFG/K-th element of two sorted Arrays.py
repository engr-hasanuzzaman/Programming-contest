# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1/#

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if len(arr1) > len(arr2):
            return self.binaray_search(arr2, arr1, m, n, k)
        else:
            return self.binaray_search(arr1, arr2, n, m, k)

    # arr1 <= arr2
    def binaray_search(self, arr1, arr2, n, m, k):
        low = max(0, k-m)
        high = min(n, k)

        while low <= high:
            # for arr1
            cut1 = low + (high - low) // 2
            cut2 = k - cut1

            l1 = arr1[cut1-1] if cut1 > 0 else float('-inf')
            l2 = arr2[cut2-1] if cut2 > 0 else float('-inf')
            r1 = arr1[cut1] if cut1 < n else float('inf')
            r2 = arr2[cut2] if cut2 < m else float('inf')

            if l1 > r2:
                high = cut1 - 1
            elif l2 > r1:
                low = cut1 + 1
            else:
                return max(l1, l2)
