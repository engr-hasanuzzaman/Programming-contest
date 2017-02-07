# @param {Integer[]} nums
# @return {String[]}
def find_relative_ranks(nums)
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    positions = nums.sort_by{|n| -n}.each_with_index.each_with_object({}){|(n, i), h| h[n] = medals.fetch(i, (i + 1).to_s) }
    
    result = []
    nums.each do |n|
       result << positions[n]
    end
    
    return result
end
