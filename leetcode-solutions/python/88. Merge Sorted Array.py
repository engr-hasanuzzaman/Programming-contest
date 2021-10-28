# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # add new element on the new position, fix the order
        for i in range(n):
          j = m + i
          nums1[j] = nums2[i]
          while j > 0 and nums1[j-1] > nums1[j]:
            nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
            j -= 1

# time complexity m + n
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        # take only data part to prevent from override
        data_from1 = nums1[:m]
        while i < m and j < n:
            if  i < m and data_from1[i] <= nums2[j]:
                while i < m and data_from1[i] <= nums2[j]:
                    nums1[k] = data_from1[i]
                    k += 1
                    i += 1
            else:
                while j < n and data_from1[i] >= nums2[j]:
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1

        # fill the remaining items
        if i != m or j != n:
            if i < m:
                for h in range(i, m):
                    nums1[k] = data_from1[h]
                    k += 1
            else:
                for h in range(j, n):
                    nums1[k] = nums2[h]
                    k += 1
                    