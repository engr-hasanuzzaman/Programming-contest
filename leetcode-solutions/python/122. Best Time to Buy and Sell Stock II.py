# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# since we can sell and buy at the same date, we can do greedy choice
# if next day price is greater, buy today and sell tomorrow and if price in day after tomorrow is
# greater than tomorrwo, will buy tomorrw 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
            i += 1
        return profit
