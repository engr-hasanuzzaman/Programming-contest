# https://leetcode.com/problems/k-th-symbol-in-grammar/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_grammar(n, k)
  return 0 if n == 0
  if kth_grammar(n-1, (Float(k)/2).ceil) == 1
     if  k % 2 == 0
         return 0
     else
         return 1
     end
  else
      if  k % 2 == 0
         return 1
     else
         return 0
     end
  end
end