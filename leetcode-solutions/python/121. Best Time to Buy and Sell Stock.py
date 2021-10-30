# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0]
        max_profit = 0
        for p in prices:
            min_buy_price = min(p, min_buy_price)
            max_profit = max(max_profit, p - min_buy_price)
        return max_profit
