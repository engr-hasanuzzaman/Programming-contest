
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/submissions/

# if the subarray has even number of negative numbers, the whole subarray has positive product.
# Otherwise, we have two choices, either 
# 1. remove the prefix till the first negative element in this subarray, or 
# 2. remove the suffix starting from the last negative element in this subarray.
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def find_max_length(nums):
            neg_index = []
            neg_count = 0
            for i, n in enumerate(nums):
                if n < 0:
                    neg_count += 1
                    neg_index.append(i)
            if neg_count % 2 == 0:
                return len(nums)
            else:
                # prefix = len(nums) - first_neg_index - 1 // [1,2,-3....] -> 
                # for suffix last_index will indicate number before suffix
                return max(len(nums) - neg_index[0] - 1, neg_index[-1])
    
        max_length = 0
        last_non_zero = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            
            # either all element visited of zero found, befor ith number are valid
            # if first elemet is zero, calculate length or empty arrat
            max_length = max(max_length, find_max_length(nums[last_non_zero:i]))
            # i + 1 is our next valid element
            i += 1
            last_non_zero = i
        return max_length
                
            
                
        