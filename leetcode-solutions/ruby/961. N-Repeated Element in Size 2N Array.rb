# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# @param {Integer[]} a
# @return {Integer}
def repeated_n_times(a)
  n_hash = Hash.new(0)
  a.each do |e|
      return e if n_hash[e] > 0
      n_hash[e] += 1
  end
end