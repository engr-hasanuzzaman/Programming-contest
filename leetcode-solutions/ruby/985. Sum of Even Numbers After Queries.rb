# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

# @param {Integer[]} a
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(a, queries)
  even_sum = a.select(&:even?).sum
  answer = []
  queries.each do |q|
      v, i = q
      
      if a[i].even? && v.even?
          even_sum += v
      elsif a[i].odd? && v.odd?
          even_sum += a[i] + v
      elsif a[i].even?
          even_sum -= a[i]
      end
      
      a[i] += v
      answer << even_sum
  end
  
  answer
end