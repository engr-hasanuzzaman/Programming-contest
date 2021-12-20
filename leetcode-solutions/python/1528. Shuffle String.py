# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(s)
        i = 0
        for _, j in enumerate(indices):
            ans[j] = s[i]
            i += 1
        return "".join(map(str, ans))
