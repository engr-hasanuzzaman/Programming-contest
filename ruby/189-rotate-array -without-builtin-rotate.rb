# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
# here I have use str rever technique for rotating
# examp, [1,2,3,4], rotate 2
# first rev return [4,3,2,1]
# second rev return [3,4,2,1]
# last rev return [3,4,1,2]

def rotate(nums, k)
    # return if nums has only one value or actual rotation is zero
    return nums if nums.size < 1 || (k % nums.size) == 0
    
    actual_rotation = k % nums.size
    
    nums.reverse!
    nums.reverse_with_range(0, actual_rotation - 1)
    nums.reverse_with_range(actual_rotation, nums.size - 1)
end


class Array
    def reverse_with_range(start_index, end_index)
        while(start_index < end_index) do
            self[start_index], self[end_index] = self[end_index], self[start_index]
            start_index += 1
            end_index -= 1
        end
    end
end
