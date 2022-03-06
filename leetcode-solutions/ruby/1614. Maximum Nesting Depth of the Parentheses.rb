# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


# @param {String} s
# @return {Integer}
def max_depth(s)
    stack = []
     max_nesting = 0
     s.each_char do |chr|
         if chr == '('
             stack << chr
         elsif chr == ")"
             stack.pop
         end
     
         max_nesting = [max_nesting, stack.size].max
     end
     
     max_nesting
 end
 