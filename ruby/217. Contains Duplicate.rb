# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    nums.each_with_object(Hash.new(0).merge dup: []){|n, h| h[:dup] << n if (h[n] += 1) >= 2}[:dup].size > 0
end
