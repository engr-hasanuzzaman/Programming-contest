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

# more faster with sorting the candidate
def combination_sum(candidates, target)
  ans = []
  combination(candidates.sort, target, ans, [])
  ans.uniq
end

def combination(candidates, target, ans, cur_list)
  if target.zero?
      ans << cur_list.map{|e| e}.sort
  end
  
  if candidates.first > target || target < 0
      return
  end
  
  candidates.each do |candidate|
      cur_list << candidate
      combination(candidates, target - candidate, ans, cur_list)
      cur_list.pop
  end
end