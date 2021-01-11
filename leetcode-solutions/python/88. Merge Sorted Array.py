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