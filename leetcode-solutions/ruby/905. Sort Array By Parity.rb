# https://leetcode.com/problems/sort-array-by-parity/

# @param {Integer[]} a
# @return {Integer[]}
def sort_array_by_parity(a)
  a.select(&:even?) + a.select(&:odd?)
end