'''

Given a binary array, find the index of 0 to be replaced with 1 to get the maximum length sequence of continuous ones. The solution should return the index of first occurence of 0, when multiple continuous sequence of maximum length is possible.

Input : [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
Output: 7
Explanation: Replace index 7 to get the continuous sequence of length 6 containing all 1’s.

Input : [0, 1, 1, 0, 0]
Output: 0
Explanation: Replace index 0 or 3 to get the continuous sequence of length 3 containing all 1’s. The solution should return the first occurence.

Input : [1, 1]
Output: -1
Explanation: Invalid Input (all 1’s)

'''

class Solution:
	def findIndexofZero(self, nums: List[int]) -> int:
		# Write your code here...
		continuous_neighbors = [0] * len(nums)
		cur_count = 0
		zero_count = 0
		for i, n in enumerate(nums):
			if n == 0:
				continuous_neighbors[i] += cur_count
				cur_count = 0
				zero_count += 1
			else:
				cur_count += 1
		if zero_count == 0: return -1
		cur_count = 0
		
		for i in range(len(nums) - 1, -1, -1):
			if nums[i] == 0:
				continuous_neighbors[i] += cur_count
				cur_count = 0 
			else:
				cur_count += 1
		cur_max = 0
		max_index = 0
		for i in range(len(nums)):
			if continuous_neighbors[i] > cur_max:
				cur_max = continuous_neighbors[i]
				max_index = i
		return max_index
