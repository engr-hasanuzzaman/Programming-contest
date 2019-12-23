# https://leetcode.com/problems/decode-string/

# @param {String} s
# @return {String}
def decode_string(s)
  stack = []
  
  s.each_char do |c|
      str = ''
      if c == ']' 
          while stack.last != '[' && !stack.empty?
              str = stack.pop + str
          end
          # remove [
          stack.pop
          
          # num
          num = ''
          while is_num?(stack.last)
            num = stack.pop + num     
          end
          
          # puts "#{n} #{str}"
          str = str * num.to_i
          stack << str
      else
          stack << c
      end
  end
  stack.join('')
end
  
def is_num?(c)
  ('0'..'9').include?(c)
end