# https://leetcode.com/problems/squares-of-a-sorted-array/

# @param {Integer[]} a
# @return {Integer[]}
def sorted_squares(a)
  a.map{|n| n**2}.sort
end