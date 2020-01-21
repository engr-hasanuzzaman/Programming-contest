# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  profit = 0
  i = 0
  while i < prices.size - 1
      if prices[i+1] > prices[i]
          profit += prices[i+1] - prices[i]
      end
      
      i += 1
  end
  
  profit
end