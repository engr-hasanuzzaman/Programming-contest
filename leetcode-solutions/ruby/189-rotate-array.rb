# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    # return if nums has only one value or actual rotation is zero
    return nums if nums.size < 1 || (k % nums.size) == 0
    
    actual_rotation = k % nums.size
    
    # use ruby array rotate method that defaultly rotate left
    nums.rotate!(-actual_rotation)
end
