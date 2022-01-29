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