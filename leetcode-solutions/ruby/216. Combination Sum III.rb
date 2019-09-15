# https://leetcode.com/problems/combination-sum-iii/

# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
def combination_sum3(k, n)
  result = []
   comb = []
   combination(result, comb, k, n, 1)
   result
end

def combination(result, comb, k, n, start_index)
   if k == 0 && n == 0
       result << comb.map{|i| i}
   end
   
   if k > 0 && n > 0 && n >= start_index
       start_index.upto(9) do |i|
           comb << i
           combination(result, comb, k-1, n-i, i+1)
           comb.pop
       end
   end
end