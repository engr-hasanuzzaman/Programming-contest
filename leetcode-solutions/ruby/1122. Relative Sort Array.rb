# https://leetcode.com/problems/relative-sort-array/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def relative_sort_array(arr1, arr2)
  arr1_hash = Hash.new(0)
   
   arr1.each do |i|
       arr1_hash[i] += 1
   end
   
   result = []
   # puts "---#{arr1_hash}"
   arr2.each do |n|
       arr1_hash[n].times{ result << n }
       arr1.delete(n)
   end
   
   result += arr1.sort
   result
end