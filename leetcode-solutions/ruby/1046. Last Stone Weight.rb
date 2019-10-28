# https://leetcode.com/problems/last-stone-weight/
# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
  stones = stones.sort
  
  while stones.size > 1
      y, x = stones[-1], stones[-2]
      if x == y
          stones = stones[0...-2]
      else
          stones = stones[0...-2]
          stones << y - x
          stones.sort!
      end
  end
  
  stones.first
end