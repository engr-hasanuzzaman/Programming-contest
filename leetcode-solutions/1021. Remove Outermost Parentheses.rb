#https://leetcode.com/problems/remove-outermost-parentheses/submissions/

# @param {String} s
# @return {String}
def remove_outer_parentheses(s)
  primitive = ''
  result = ''
  s_size = s.size     
  p_counter = 0
  
  s.each_char do |c|    
    if c == "("
        p_counter += 1 
    else
        p_counter -= 1 
    end
    
    primitive += "#{c}"
    
    if p_counter.zero?
        result += primitive[1..-2]
        primitive = ''
    end     
            
  end
  
  result
end