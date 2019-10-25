# https://leetcode.com/problems/reverse-string-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def reverse_str(s, k)
  s_i = 0
  rev = true
  res = ''
  while s_i < s.size do
      if rev
         res += s[s_i...s_i+k].reverse
          rev = false
      else
          rev = true
          res += s[s_i...s_i+k]
      end
      
      s_i += k
  end
  
  res
end