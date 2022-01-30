# https://leetcode.com/problems/contains-duplicate-iii/

# TLE solution with complexity N*K where N is the size of array
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and j <= i+k:
                if abs(nums[j] - nums[i]) <= t:
                           return True
                j += 1
        return False

# AC with sliding window and bucket
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2 or t < 0 or k < 1:
            return False

        buckets = {}
        # The bucket size is t+1 as the ranges are from 0..t, t+1..2t+1, ..
        # if t is zero that means we supposed to have atleast one bucket
        bucket_size = t + 1
        for i, num in enumerate(nums):
            # shrink the window
            if i > k:
                last_bucket = nums[i - k - 1] // bucket_size # since allowed diff is bucket_size
                del buckets[last_bucket]

            bucket = num // bucket_size
            # if already has number in this same bucket
            # ex. number 20, 24 with t = 5 will be in the same bucket
            if bucket in buckets:
                return True
            
            # check the neiboring bucket 
            # 20, 19 will be in a different bucket
            if (bucket - 1) in buckets and num - buckets[bucket - 1] <= t:
                return True
            
            # 29, 30 will be on the different bucket
            if (bucket + 1) in buckets and buckets[bucket + 1] - num <= t:
                return True
                
            buckets[bucket] = num
        return False
        