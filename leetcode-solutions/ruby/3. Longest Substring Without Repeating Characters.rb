# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# @param {String} s
# @return {Integer}
def length_of_longest_substring(str)
  sub_str = []
  max_sub_str_len = 0
  
  str.each_char do |char|
    char_index = sub_str.index char
    
    if char_index
      sub_str = sub_str[char_index + 1..-1] #remove part from char
      sub_str << char
    else
      sub_str << char
    end
    sub_str_size = sub_str.size
    max_sub_str_len = sub_str_size if max_sub_str_len < sub_str_size
  end
  
  max_sub_str_len
end