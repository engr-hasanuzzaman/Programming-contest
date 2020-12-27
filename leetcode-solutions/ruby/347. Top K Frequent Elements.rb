# https://leetcode.com/problems/top-k-frequent-elements/
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    dict = {}
     nums.each do |n|
         if dict[n]
             dict[n] += 1
         else
             dict[n] = 1
         end
     end
   processed_input = []
   dict.keys.each do |k|
       processed_input << [dict[k], k]
   end
     processed_input.sort_by{|a| -a.first}.take(k).map{|e| e.last}
 end