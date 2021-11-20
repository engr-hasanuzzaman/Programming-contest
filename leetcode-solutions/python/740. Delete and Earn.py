# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        count = {}
        uniq_nums = []
        for i in range(len(nums)):
            n = nums[i]
            if n in count:
                count[n] += n
            else:
                uniq_nums.append(n)
                count[n] = n
        
        dp = {}
        for i in range(len(uniq_nums)):
            n = uniq_nums[i]
            
            # if first, pick sum
            if i == 0:
                dp[n] = count[n]
            elif i == 1:
                # if prv number was immediate prev number
                if uniq_nums[i - 1] == n - 1:
                    dp[n] = max(dp.get(n-1, 0), count[n])
                else:
                    dp[n] = count[n] + dp.get(uniq_nums[i - 1], 0)
            else:
                # if prv number was immediate prev number
                if uniq_nums[i - 1] == n - 1:
                    dp[n] = max(dp.get(n-1, 0), count[n] + dp[uniq_nums[i - 2]])
                else:
                    # diff btw prv value was > 1, that value will be added
                    dp[n] = count[n] + dp[uniq_nums[i - 1]]
            
        return dp[uniq_nums[-1]]
