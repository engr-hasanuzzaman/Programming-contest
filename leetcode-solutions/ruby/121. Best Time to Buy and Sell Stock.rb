#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  min_price = Float::MAX
  max_profit = 0
  
  prices.each do |v|
      if v < min_price
          min_price = v
      elsif v - min_price > max_profit
          max_profit = v - min_price
      end
  end
  
  max_profit
end