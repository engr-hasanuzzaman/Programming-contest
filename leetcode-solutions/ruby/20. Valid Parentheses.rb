# https://leetcode.com/problems/valid-parentheses/

# @param {String} s
# @return {Boolean}
def is_valid(str)
  return true if str.size.zero?
  # stack for keeping last val
  s = []
  
  str.each_char do |c|
      if s.last
          if valid?(s.last, c)
              s.pop
          else
              s << c
          end
      else
          s << c
      end
  end
  
  s.empty?
end
  
def valid?(c1, c2)
  if (c1 == ")" && c2 == "(") || ( c2 == ")" && c1 == "(")
      return true
  elsif (c1 == "}" && c2 == "{") || ( c2 == "}" && c1 == "{")
      return true
  elsif (c1 == "]" && c2 == "[") || ( c2 == "]" && c1 == "[")
      return true
  else
      return false
  end
end

# smaller code size
# @param {String} s
# @return {Boolean}
def is_valid(s)
    stack = []
    pair_dict = {
        '}' => '{',
        ')' => '(',
        ']' => '['
    }
    s.each_char do |char|
        if char == '(' || char == '{' || char == '['
            stack.push(char)
        else
            return false if stack.empty? or pair_dict[char] != stack.last
            stack.pop
        end
    end
    
    return stack.empty?
end