# https://leetcode.com/problems/next-permutation/

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def next_permutation(nums)
    i = nums.size - 1
    while i > 0 && nums[i-1] >= nums[i]
        i -= 1
    end
    
    # nums are in decreasing order
    if i == 0
        reverse(0, nums)
        return nums
    end
    
    k = i - 1 # bounding element of the arrangement
    # since ith to end are in decreasing order
    # ther might another smaller number which is greater that number in kth position
    while i < nums.size && nums[i] > nums[k]
        i += 1
    end
    
    # i - 1 is the smallest number which is > kth number
    nums[k], nums[i-1] = nums[i-1], nums[k]
    
    # since, from k+1 to end, all ther number are in decreasing order
    # reverse to make increasing to ensure it will create smallest number
    reverse(k+1, nums)
end

def reverse(idx, nums)
    start_i = idx
    end_i = nums.size - 1
    while start_i < end_i
        nums[start_i], nums[end_i] = nums[end_i], nums[start_i]
        start_i += 1
        end_i -= 1
    end
end
