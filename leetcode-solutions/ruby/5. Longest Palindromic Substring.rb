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

# using expand from the middle option
# @param {String} s
# @return {String}
def longest_palindrome(s)
    s_idx = e_idx = 0
    n = s.size
    n.times do |i|
        l1 = expand_from_middle(s, i, i) # will cover aba
        l2 = expand_from_middle(s, i, i + 1) # will cover abba
        len = [l1, l2].max
        if len > e_idx - s_idx
            s_idx = i - (len - 1) / 2
            e_idx = i + (len / 2)
        end
    end
    
    s[s_idx..e_idx]
end

def expand_from_middle(s, left, right)
    return 0 if s.size.zero? || left > right
    
    while left >= 0 && right < s.size && s[left] == s[right]
        left -= 1
        right += 1
    end
    
    right - left - 1
end