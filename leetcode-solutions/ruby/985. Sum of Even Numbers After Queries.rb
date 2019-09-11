# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

# @param {Integer[]} a
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(a, queries)
  even_sum = a.select(&:even?).sum
  answer = []
  queries.each do |q|
      v, i = q
      if a[i].even?
          even_sum += v
      end
      
      answer << even_sum
  end
  
  answer
end