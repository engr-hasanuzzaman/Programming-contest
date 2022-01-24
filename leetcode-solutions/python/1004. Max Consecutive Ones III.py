# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count, cur_count = 0, 0
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] == 1:
                cur_count += 1
            elif k > 0:
                k -= 1
                cur_count += 1
            else:
                # remove zero from the left utill k become positive
                while k <= 0:
                    if nums[left] == 0:
                        k += 1
                    cur_count -= 1
                    left += 1

                # process the current zero
                cur_count += 1
                k -= 1
            right += 1
            max_count = max(max_count, cur_count)
        return max_count
        
        