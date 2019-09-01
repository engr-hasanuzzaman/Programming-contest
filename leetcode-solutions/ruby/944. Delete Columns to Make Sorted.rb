# https://leetcode.com/problems/delete-columns-to-make-sorted/

# @param {String[]} a
# @return {Integer}
def min_deletion_size(a)
  d_count = 0
  
  a[0].size.times do |i|
      c_char = nil
      p_char = nil
      
      a.size.times do |j|
          p_char = c_char
          c_char = a[j][i]
          
          next unless p_char
          
          if p_char > c_char
              d_count += 1
              break
          end
      end
  end
  
  d_count
end