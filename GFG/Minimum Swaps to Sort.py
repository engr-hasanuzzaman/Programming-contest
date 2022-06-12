class Solution:
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        num_idx_tuples = [(num, idx) for idx, num in enumerate(nums)]
        num_idx_tuples.sort()
        idx = 0
        count = 0
        while idx < len(nums):
            if num_idx_tuples[idx][1] != idx:
                old_idx = num_idx_tuples[idx][1]
                num_idx_tuples[idx], num_idx_tuples[old_idx] = num_idx_tuples[old_idx], num_idx_tuples[idx]
                count += 1
            else:
                idx += 1
        return count
