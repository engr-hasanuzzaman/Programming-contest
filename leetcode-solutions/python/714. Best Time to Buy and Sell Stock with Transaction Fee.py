# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif prices[i] - min_price - fee > 0:
                profit += prices[i] - min_price - fee
                """
                for the case [1,8,9], when we get 8 we want to sell as we are getting profit (greedy choic) 
                but after this we might have greater value so instead of making sell on 8, making sell on 9 is
                more profitable (since we have transaction fee). 
                How do we know we might have greater value which will be more profitable? or how to add extra amount 
                with the current profit? 
                so during setting the new min_price we will sub-track the fee so that we get higher value we do not need to give
                the transaction fee again or we might get small value, to buy that time will be more profitable.
                In other word if (next value is < current - fee) using new transaction will be profitable
                """
                min_price = prices[i] - fee
        return profit
        
