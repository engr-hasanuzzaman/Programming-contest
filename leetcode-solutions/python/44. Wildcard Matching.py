# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # with empty string and empty pattern, return is True
        dp[0][0] = True

        # match * with empty
        for j in range(1, len(dp[0])):
            # if current char is *, final result is previous result
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # dp[i][j-1] contains result if we ignore current *
                    # dp[i-1][j-1] if we consider * is = to current char
                    # dp[i-1][j] if we consider * is part of wildcard
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
    
        return dp[-1][-1]