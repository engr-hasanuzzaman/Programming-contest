# https://leetcode.com/problems/word-pattern/

# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
  s_array = str.split
  
  return false if s_array.size != pattern.size
  
  s_pattern = {}
  w_pattern = {}
  
  pattern.each_char.with_index do |c, i|
    if (s_pattern[c] && s_pattern[c] != s_array[i]) || (w_pattern[s_array[i]] && w_pattern[s_array[i]] != c)
      return false 
    end
  
    s_pattern[c] = s_array[i]
    w_pattern[s_array[i]] = c
  end
  
  true
end