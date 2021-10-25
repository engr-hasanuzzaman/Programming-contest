# https://leetcode.com/problems/3sum/

'''
use two pointer technique to find the two sum calculation and use that to calcumate the 3 sum
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        
        def twoSum(elm, s, e = len(nums) - 1):
            while s < e:
                if nums[s] + nums[e] + elm > 0:
                    e -= 1
                elif nums[s] + nums[e] + elm < 0:
                    s += 1
                else:
                   # sum of two is expected elm                     
                    comb = [elm, nums[s], nums[e]]
                    if not comb in ans:
                        ans.append(comb)
                    s += 1
                    e -= 1
        
        for i in range(length - 2):
            twoSum(nums[i], i + 1)
        return ans
            
                
        
            
            