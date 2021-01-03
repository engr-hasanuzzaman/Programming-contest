def partition(nums)
    sum = nums.sum
    # puts "sum #{sum}"
    half = (sum.to_f/2).ceil
    memo = {}
    memo['optimal_sub_sum']   
      
    # return false if sum.odd?
    # return true if nums.include?(half)
  
    optimal_half = calculate_min_diff(memo, nums, 0, half).abs
    # puts "--------------------------------------"
    # puts "memo is #{memo}"
    [half + optimal_half, sum - half - optimal_half].sort_by{|e| -e}.join(" ")
end
  
def calculate_min_diff(memo, nums, i, sum)
    memo_key = "#{i}_#{sum}"

    # most expected value
    if sum == 0
        memo['optimal_sub_sum'] = sum
        memo['memo_key'] = sum
        return memo['memo_key']
    end

    # handle exceed expected value or index
    if i >= nums.size || sum < 0
        memo[memo_key] = sum
        return memo[memo_key]
    end

    with_current_value = calculate_min_diff(memo, nums, i+1, sum-nums[i])  
    without_current_value = calculate_min_diff(memo, nums, i+1, sum)
    if (with_current_value).abs > (without_current_value).abs
        memo[memo_key] = without_current_value
    else
        memo[memo_key] = with_current_value
    end

    memo[memo_key]
end

ans = []
ARGF.each_line do |line|
    if line === '0' || line === 0
        break
    end
    nums = line.split().map(&:to_i)
    ans << partition(nums)
end

ans.each {|o| puts o}
