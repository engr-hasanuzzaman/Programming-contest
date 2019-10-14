# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# @param {String} s
# @return {Integer}
def balanced_string_split(s)
  number = 0
  b_str_found = nil
  
  0.upto(s.size-1) do |i|
      if s[i] == 'R'
              b_str_found = b_str_found.to_i + 1
      else
          b_str_found = b_str_found.to_i - 1
      end

      if b_str_found.zero?
          number += 1
      end
  end
  
  number
end