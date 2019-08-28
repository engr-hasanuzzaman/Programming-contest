# https://leetcode.com/problems/di-string-match/submissions/

# @param {String} s
# @return {Integer[]}
def di_string_match(s)
  l_index = s.size
  s_index = 0
   result = []
   s.each_char do |c|
      if c == 'D'
          result << l_index
          l_index -= 1
      else
          result << s_index
          s_index += 1
      end
   end
   
   if s[s.size-1] == 'D'
       result << s_index
   else
       result << l_index
   end
   
   result
end