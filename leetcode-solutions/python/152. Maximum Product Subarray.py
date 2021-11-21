# https://leetcode.com/problems/maximum-product-subarray/
# for the max produc, since negetive number can generate max sum, we will keep min & max both
# and multiply nums[i] with both min & max to get the max number possible
# cur_max = max(nums[i], min_number * nums[i], max_number * nums[i])
# cur_min = min(nums[i], min_number * nums[i], max_number * nums[i])
# min_number = cur_min
# max_number = cur_max
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max_product_till_now = min_product_till_now = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            cur_max_product_till_now = max(nums[i], nums[i] * max_product_till_now, min_product_till_now * nums[i])
            cur_min_product_till_now = min(nums[i], nums[i] * max_product_till_now, min_product_till_now * nums[i])
            max_product_till_now = cur_max_product_till_now
            min_product_till_now = cur_min_product_till_now
            max_product = max(max_product, max_product_till_now)
        return max_product
