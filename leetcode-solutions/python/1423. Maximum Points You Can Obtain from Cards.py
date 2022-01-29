# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# TLE solution with back tracking with memoizition
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def max_point(cards, start, end, cur_sum, k):
            key = str(start) + "_" + str(end) + "_" + str(k)
            if key in self.memo:
                return self.memo[key]

            if k == 0:
                self.memo[key] = cur_sum
                self.max_sum = max(self.max_sum, cur_sum)
                return self.memo[key]
            # print(start, end, cur_sum, k)
            max_picking_start = max_point(cards, start+1, end, cur_sum + cards[start], k - 1)
            max_picking_end = max_point(cards, start, end - 1, cur_sum + cards[end], k - 1)
            self.memo[key] = max(max_picking_start, max_picking_end)
            return self.memo[key]
        self.memo = {}
        self.max_sum = 0
        max_point(cardPoints, 0, len(cardPoints) - 1, 0, k)
        return self.max_sum

# solve using sliding window
# What is asked in this problem: we need to take some numbers and some numbers from the beginning, 
# such that the sum of therse taken k numbers are maximal. 
# It is equivalent to take n - k adjacent numbers with minimal sum and then return sum of all numbers minus this value.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = 0
        min_sum = float('inf')
        cur_sum = 0
        start = 0
        size =  len(cardPoints) - k # sub-array size for which sum is min
        
        for index, point in enumerate(cardPoints):
            total_sum += point
            cur_sum += point
            if size > 0 and index >= size - 1:
                min_sum = min(min_sum, cur_sum)
                cur_sum -= cardPoints[start]
                start += 1
        # print(min_sum, total_sum)
        if size == 0: return total_sum
        return total_sum - min_sum

# another solution with time complexity O(k)
'''
For convenience's sake I'll be referring to the beginning and the end of the row of cards as the left and right side respectively.

For any given array of cards we can take n cards from the left side and m cards from the right side where n, m are non-negative integers and n + m = k.
So we simply need to look through every pair of n and m to determine the max sum of k cards.

Our initial step will be finding the sum of k cards all taken from the left side.
On every iteration step we'll be subtracting a value from the left and adding a value from the right.
This way we can avoid using sum() saving our ever so precious processing time.

Once we get to the sum of k cards all taken from the right side, we will have checked every possible pair of n and m.

So, for example:
cardPoints = [1, 2, 3, 4, 5, 6, 7], k = 3
[1, 2, 3], 4, 5, 6, 7 : Initial state, cursum = 6, next comes iteration
1, 2], 3, 4, 5, 6, [7 : 1. subtract 3 and add 7, now cursum = 10
1], 2, 3, 4, 5, [6, 7 : 2. subtract 2 and add 6, now cursum = 14
1, 2, 3, 4, [5, 6, 7] : 3. subtract 1 and add 5, now cursum = 18
Iteration done in 3 = k steps.

The answer will be the greatest value of cursum, which in this case equals 18. This can easily be handled by another variable.
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        max_sum = cur_max = sum(cardPoints[:k])
        if length == k:
            return max_sum
        
        for i in range(k):
            cur_max = cur_max - cardPoints[k - i - 1] + cardPoints[length - i - 1]
            max_sum = max(max_sum, cur_max)
        return max_sum
