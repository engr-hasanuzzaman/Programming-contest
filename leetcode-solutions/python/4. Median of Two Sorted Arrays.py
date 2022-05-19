# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.binary_search(nums2, nums1)
        else:
            return self.binary_search(nums1, nums2)

    # considering arr1 is smaller array
    def binary_search(self, arr1, arr2):
        N1 = len(arr1)
        N2 = len(arr2)
        # print(f"size1 {N1}, {N2}")
        # controller postion for array one
        lo = 0
        hi = N1

        while lo <= hi:
            # num of elements which will be taken from arr1 on left side
            # if we divide final array into two parts equal number, both firt and  2nd parts will have same number of elements
            # how many of that number will come from first array we do not know, if we know we can calculate
            # how many number come from 2nd array in frist part, similarly on the 2nd part
            cut1 = lo + (hi - lo) // 2
            cut2 = (N1+N2) // 2 - cut1

            # l1, l2 are the last num from arr1 & arr2 for first half
            # r1, r2 are the first num from arr1 & arr2 from last half
            l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
            r1 = float('inf') if cut1 == N1 else arr1[cut1]
            r2 = float('inf') if cut2 == N2 else arr2[cut2]

            # print(f"--c1: {cut1}, c2: {cut2}, l1: {l1}, {l2}, {r1}, {r2}")
            # condition
            # l1 < r2 and l2 < r1 is our expected scenario
            if l1 > r2:
                hi = cut1 - 1
            elif l2 > r1:
                lo = cut1 + 1
            else:
                # print(f" ans for {arr1}, {arr2}, {l1}, {l2}, {r1}, {r2}")
                if (N1 + N2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) * 0.5
                else:
                    return min(r1, r2)
