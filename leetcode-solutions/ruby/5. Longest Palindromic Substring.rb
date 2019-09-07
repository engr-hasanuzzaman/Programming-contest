# https://leetcode.com/problems/longest-palindromic-substring/

# @param {String} s
# @return {String}
def longest_palindrome(s)
  size = s.size
  m_size = 0 # palindrom max size
  p_i = 0 # palindrom starting index
  
  # for loop i = 0 to i < s.length
  size.times do |i|
      si = i
      p_s = 1
      counter = 1
      
      # check odd number center 
      while i - counter >= 0 && s[i-counter] == s[i+counter]
          counter += 1
      end # end of while
      
      if 1 + 2 * (counter - 1) > m_size
          m_size = 1 + 2 * (counter - 1)
          p_i = i - counter + 1
          # puts "new_max size #{m_size}, p_i #{p_i}, i #{i} top"
      end
      
      # check for even number palindrom
      if s[i] == s[i+1]
          # puts "---continuous char #{i} #{s[i]} #{s[i+1]}"
          # all continuous matching
          p_s = 2
          ei = i+2 
          si = i - 1
          
          while si >= 0 && s[si] == s[ei]
              si -= 1
              ei += 1
          end
          
          ts = ei - si - 1
          
          if m_size < ts
              m_size = ts
              p_i = si + 1
              # puts "new_max size #{m_size}, p_i #{p_i}, i #{i}"
          end
          
      end
  end
  
  # return charts from p_i to (p_i + m_size - 1)
  s[p_i...p_i+m_size]
end