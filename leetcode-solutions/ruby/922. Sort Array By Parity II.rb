# https://leetcode.com/problems/sort-array-by-parity-ii/

# @param {Integer[]} a
# @return {Integer[]}
def sort_array_by_parity_ii(a)
  odd_array = []
  even_array = []
  
  a.each do |n|
      if n % 2 == 0
          even_array << n
      else
          odd_array << n
      end
  end
  
  a.size.times do |i|
      if i % 2 == 0
          a[i] = even_array.pop
      else
          a[i] = odd_array.pop
      end
  end
  
  a
end