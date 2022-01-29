# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result

# solution using dictionary/map
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = defaultdict(int)
        for num in nums1:
            memo[num] += 1
            
        ans = []
        for num in nums2:
            if memo[num] > 0:
                ans.append(num)
                memo[num] -= 1
        return ans
