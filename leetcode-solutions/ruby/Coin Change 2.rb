# inprogress 

# -----using back tracking---------
# N.B: Timelimit exit
# @param {Integer} amount
# @param {Integer[]} coins
# @return {Integer}
def change(amount, coins)
  return 0 if amount.zero?
  
  dp = []
  coins = coins.uniq.sort_by{|n| -n}
  ans = []
  comb = []
  cal(coins, amount, ans, comb)
  p ans
  ans.uniq.size
end

def cal(coins, target, ans, comb)
  # puts "target #{target}, #{comb.inspect}"
  if target == 0
      ans << comb.sort
      return
  end
      
  coins.each do |c|
      if target - c < 0
          next
      end
      
      comb << c
      cal(coins, target - c, ans, comb)
      comb.pop
  end
end


# dp with reduce memory
def change(amount, coins)
  dp = Array.new(amount+1){0}
  dp[0] = 1
  coins.each do |c|
      for a in c..amount
          dp[a] += dp[a-c] 
      end
  end
  
  dp[amount]
end
