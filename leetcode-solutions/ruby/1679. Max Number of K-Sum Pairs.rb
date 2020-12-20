# Problem link: https://leetcode.com/problems/max-number-of-k-sum-pairs/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_operations(nums, k)
    dict = {}
    operations = 0
    nums.each do |num|
        rem = k - num
        if dict[rem]
            # p dict
            if dict[rem] > 0
                operations += 1
                dict[rem] -= 1
            else
                if dict[num]
                    dict[num] += 1
                else
                    dict[num] = 1
                end
            end
        else
            if dict[num]
                dict[num] += 1
            else
                dict[num] = 1
            end
        end
    end
    
    operations
end