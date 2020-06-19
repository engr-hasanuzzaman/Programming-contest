# https://leetcode.com/problems/coin-change/

# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
  if amount == 0
      return 0
  end
  
  memo = {}
  dp(coins.sort, amount, memo)
end

def dp(coins, amount, memo)
  return 0 if amount.zero?
  return memo[amount] if memo[amount]
  return -1 if amount < coins.first
  ans = []
  for coin in coins
      if amount - coin >= 0
          t = dp(coins, amount - coin, memo)
          memo[amount-coin] = t
          ans << t + 1 unless t == -1
      else
          break
      end
  end

  if ans.size.zero?
      return -1
  else
      memo[amount] = ans.min
      memo[amount]
  end
end

