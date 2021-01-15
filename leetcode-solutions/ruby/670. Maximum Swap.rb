# https://leetcode.com/problems/maximum-swap/
=begin
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
=end
def maximum_swap(num)
    nums = num.to_s.split("").map(&:to_i)
    last = {}
    # keep track of last appearence of each number
    nums.each_with_index do |n,i|
        last[n] = i
    end
    
    # loop over each number
    nums.each_with_index do |n, i|
        # since valid number are 9-0 and we will check where max digit is exist
        # but on the later index so, swapping two will give max value
        9.downto(n+1) do |d|
        if last[d] && last[d] > i
            nums[last[d]], nums[i] = nums[i], nums[last[d]]
            return nums.join.to_i
        end
        end
    end
    num
end