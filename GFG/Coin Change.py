class Solution:
    def count(self, S, m, n): 
        memo = {}
        memo['count'] = 0
        current = [] 
        Solution.back_tracking(S, n, memo, current)
        return memo['count']

    def back_tracking(coins, target, memo, current):
        if target < 0:
            return
        
        if target == 0:
            s = "".join(map(str, sorted(current)))
            if s not in memo:
                memo[s] = True
                memo['count'] = memo['count'] + 1
            return 
        
        for coin in coins:
            current.append(coin)
            Solution.back_tracking(coins, target - coin, memo, current)
            current.pop()
    