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
