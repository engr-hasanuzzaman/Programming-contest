# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @param {Integer} d
# @return {Integer}
def find_the_distance_value(arr1, arr2, d)
  count = 0
  arr2 = arr2.sort
  arr1.each do |n1|
      if arr2.select{|n2| (n1 - n2).abs <= d }.size == 0
          count += 1
      end
  end
  
  count
end