# https://leetcode.com/problems/string-to-integer-atoi/

# @param {String} str
# @return {Integer}
def my_atoi(str)
  # valid_num = (0..9).to_a
  # valid_char = valid_num + ['+', '-']
  # str = str.gsub(' ', '')
  # return 0 if str.size.zero? || !valid_char.include?(str[0])
  
  i = str.to_i
  if i < -2147483648
      return -2147483648
  end
  
  if i > 2147483647
      return 2147483647
  end
  i
end