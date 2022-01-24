# https://leetcode.com/problems/longest-nice-substring/

# bruit force process
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # for all the sub-string, we will check isNice or not
        # we will try from larger string to smaller string
        for size in range(len(s), 1, -1):
            for start in range(len(s) - size + 1):
                string = s[start:start+size]
                if self.isNice(string):
                    return string
        return ""
    def isNice(self, s):
        memo = defaultdict(lambda: False)
        for _, c in enumerate(s):
            memo[c] = True
        for _, c in enumerate(s):
            if not (memo[c.upper()]  and memo[c.lower()]):
                return False
        return True
