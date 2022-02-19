# https://leetcode.com/problems/product-of-array-except-self/

# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    product = []
    
    current_total_product = 1
    nums.size.times do |i|
        product[i] = current_total_product
        current_total_product *= nums[i] if i < nums.size - 1
    end
    
    current_total_product = 1
    (nums.size - 1).downto(0) do |i|
        product[i] = current_total_product * product[i]
        current_total_product *= nums[i] if i > 0
    end
    
    product
end
