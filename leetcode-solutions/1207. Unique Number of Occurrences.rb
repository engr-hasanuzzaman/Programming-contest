# https://leetcode.com/problems/unique-number-of-occurrences/

# @param {Integer[]} arr
# @return {Boolean}
def unique_occurrences(arr)
  n_counter = Hash.new(0)
  
  arr.each do |n|
      n_counter[n] += 1
  end

  n_counter.values.size == n_counter.values.uniq.size
end