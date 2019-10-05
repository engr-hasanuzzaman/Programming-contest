# https://leetcode.com/problems/string-to-integer-atoi/

# @param {String} str
# @return {Integer}
def my_atoi(str)
  valid_num = (0..9).map(&:to_s)
  valid_char = valid_num + ['+', '-']
  str = str.strip
  # puts "input #{str}"
  return 0 if str.size.zero? || !valid_char.include?(str[0])
  
  num = 0
  sign = true
  
  # handle first char
  if str[0] == '+'
      sign = true
  elsif str[0] == '-'
      sign = false
  else
      num = str[0].ord - '0'.ord
  end
  # puts "sign #{sign}"
  # num = -num unless sign
  
  1.upto(str.size-1) do |i|
      c = str[i]
      break unless valid_num.include?(c)
      
      t_n = c.ord - '0'.ord
      num = num * 10 + t_n
      
      # puts "num #{num}"
      if !sign && -num < -2147483648
          return -2147483648
      end
  
      if sign && num > 2147483647
          return 2147483647
      end
      
  end
  
  
  sign ? num : -num
end