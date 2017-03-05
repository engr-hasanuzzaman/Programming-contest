# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    nums.each_with_object(Hash.new(0).merge dup: []){ |n, h| h[:dup] << n if (h[n] += 1) >= 2 }[:dup][0]
end
