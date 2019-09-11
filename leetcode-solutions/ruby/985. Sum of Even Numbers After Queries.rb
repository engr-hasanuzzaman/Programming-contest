# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

# @param {Integer[]} a
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(a, queries)
  even_sum = a.select(&:even?).sum
end