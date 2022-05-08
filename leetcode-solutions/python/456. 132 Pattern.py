# https://leetcode.com/problems/132-pattern/

# we have to find largest smller number 3rd_num after i (Ex. 1,4,2,3 for 4 -> 3 as it is > 2) if 3rd_number > current number then we have pattertn as current stack matches the 32 pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # keep largest element of the smaller numbers
        third_number = float('-inf')
        stack = []
        # think i as the middle number, third_number alrady get max of min-mumber of i-1 th number
        for i in range(len(nums) - 1, -1, -1):
            if third_number > nums[i]:
                return True

            # since number are in increment order, last poped number is the largest smaller number or nums[i]
            while stack and nums[i] > stack[-1]:
                third_number = stack.pop()
            stack.append(nums[i])
        return False
