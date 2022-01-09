# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        memo = {}
        ans = []
        for p, size in enumerate(groupSizes):
            if size in memo:
                if len(memo[size]) == size:
                    ans.append(memo[size])
                    memo[size] = [p]
                else:
                    memo[size].append(p)
            else:
                memo[size] = [p]
            
            if len(memo[size]) == size:
                ans.append(memo[size])
                memo[size] = []
        return ans
