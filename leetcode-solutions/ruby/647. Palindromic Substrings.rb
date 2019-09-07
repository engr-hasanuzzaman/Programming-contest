# https://leetcode.com/problems/palindromic-substrings/

# @param {String} s
# @return {Integer}
def count_substrings(s)
  size = s.size
  count = 0
  
  size.times do |i|
      si = i
      p_s = 1
      counter = 1
      count += 1
      
      # check odd number center 
      while i - counter >= 0 && s[i-counter] == s[i+counter]
          counter += 1
          count += 1
      end # end of while
      
      
      # check for even number
      if s[i] == s[i+1]
          # puts "---continuous char #{i} #{s[i]} #{s[i+1]}"
          # all continuous matching
          p_s = 2
          ei = i+2 
          si = i - 1
          count += 1
          
          while si >= 0 && s[si] == s[ei]
              si -= 1
              ei += 1
              count += 1
          end
          
      end
  end
  
  # puts "--- p_i #{p_i}, m_size #{m_size}"
  count
end
