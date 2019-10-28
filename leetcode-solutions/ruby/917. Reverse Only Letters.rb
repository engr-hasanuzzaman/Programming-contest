# https://leetcode.com/problems/reverse-only-letters/

# @param {String} s
# @return {String}
def reverse_only_letters(s)
  s_size = s.size
  special_char_index = {}
  c_str = ''
  valid_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  
  s.each_char.with_index do |c, i|
      if valid_char.include?(c)
          c_str << c
      else
          special_char_index[i] = c
      end
  end
  c_str.reverse!
  c_str_index = 0
  result = []
  s_size.times do |i|
      if special_char_index[i]
          result << special_char_index[i]
      else
          result << c_str[c_str_index]
          c_str_index += 1
      end
  end
  
  result.join
end