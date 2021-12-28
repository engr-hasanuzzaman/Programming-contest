# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candies = max(candies)
        for i, c in enumerate(candies):
            if c + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        