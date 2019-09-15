# https://leetcode.com/problems/combination-sum/

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
  result = []
  comb = []
  combination(result, comb, candidates, target)
  result.uniq
end

def combination(result, comb, candidates, target)
  if target == 0
      result << comb.map{|i| i}.sort
      return
  end
  
  if target > 0
      candidates.each do |c|
          comb << c
          combination(result, comb, candidates, target - c)
          comb.pop
      end
  end
end