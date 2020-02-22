# https://leetcode.com/problems/maximum-product-subarray/

# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    product = nums.first
    prev_max = product
    prev_min = product
    
    nums[1..-1].each do |n|
        cur_max = [prev_max * n, prev_min * n, n].max
        cur_min = [prev_max * n, prev_min * n, n].min
        
        prev_min = cur_min
        prev_max = cur_max
        product = [product, cur_max].max
    end

    product
end