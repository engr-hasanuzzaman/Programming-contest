# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    left_profit = [0]
    so_far_min = prices.first
    so_far_max_profit = 0
    
    prices[1..-1].each do |price|
        so_far_min = [so_far_min, price].min
        so_far_max_profit = [so_far_max_profit, price - so_far_min].max
        left_profit << so_far_max_profit
    end
    
    max_profit = 0
    so_far_max = max_cur_profit = 0
    (prices.size - 1).downto(0) do |i|
        price = prices[i]
        so_far_max = [so_far_max, price].max
        max_cur_profit = [max_cur_profit, so_far_max - price].max
        
        max_profit = [max_profit, left_profit[i] + max_cur_profit].max
    end
    
    max_profit
end
