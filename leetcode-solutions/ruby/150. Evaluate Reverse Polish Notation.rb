# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# @param {String[]} tokens
# @return {Integer}
def eval_rpn(tokens)
  stack = []
  sum = 0
  operators = %w[+ - * /]
  tokens.each do |t|
      if operators.include?(t)
          stack << operation(t, stack.pop, stack.pop)
      else
          stack << t.to_i
      end
  end
  
  stack.first
end

def operation(operator, n2, n1)
  if operator == '+'
      n1 + n2
  elsif operator == '-'
      n1 - n2
  elsif operator == '/'
      (n1.to_f / n2).to_i
  else
      n1 * n2
  end 
end