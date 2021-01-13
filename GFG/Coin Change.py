# using back tracking (Time Limit Exceed)
# Time complexity 2*N (exponential)
class Solution:
    def count(self, S, m, n): 
        memo = {}
        memo['count'] = 0
        current = [] 
        S.reverse()
        Solution.back_tracking(S, n, memo, current)
        return memo['count']

    def back_tracking(coins, target, memo, current):
        if target < 0:
            return
        
        if target == 0:
            memo['count'] = memo['count'] + 1
            return 
        
        for i in range(len(coins)):
            coin = coins[i]
            current.append(coin)
            # ensure 1,1,2 & 2,1,1 will not happen
            # if already consider larger element then do not consider that to make uniq coin cmbination
            if target - coin >= coin:
                Solution.back_tracking(coins[i:], target - coin, memo, current)
            else:
                Solution.back_tracking(coins[i+1:], target - coin, memo, current)
            current.pop()

# solve coin problem using DP
class Solution:
    def count(self, S, m, n): 
        combination = [0] * (n+1)
        # number of way we can make 0
        combination[0] = 1
        S.sort()
        # calculate numbe of way to make a particulat amount bottom-up manner
        # we will use smaller coin and build number way to make 1 to target amount
        # if amount >= coin:
        #       combination[amount] += combination[amount-coint]
        for coin in S:
            for amount in range(1, n+1):
                if amount >= coin:
                    combination[amount] += combination[amount-coin]
        return combination[n]