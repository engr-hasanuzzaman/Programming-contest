# https://leetcode.com/problems/regular-expression-matching/
# https://www.youtube.com/watch?v=l3hda49XcDE&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=10

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # using dynamic programming
        # dp[i][j] will contain result considering S[i] & P[j] matches or not
        # we will solve bottom up mannner means try to mache smallest text with patter and gradually add patter & text
        # matext of (N+1 * M+1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # empty string matches with empty pattern
        dp[0][0] = True
        
        # handle empty matching for pattern (empty S with patter P)
        # Ex. a* / a*b*c* matches with empty string
        for j in range(1, len(dp[0])):
            # dp first col is empty patter and first row is empyt string, dp 1 index means 0 in String and Pattern
            if p[j-1] == '*':
                # a* will depend on value before a* considering a* matches empty
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    # if current char match the total result is result of till pervious char match result
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # first consider empty match means without considering a* (without last two chars)
                    dp[i][j] = dp[i][j-2]
                    # if prvious char matchi with current char -> s: a, p: a* or .* (p[j-1] is *)
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # dp[i-1][j] means do not consider the current S char as it will be part of *
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    # neight char match not part of pattern
                    dp[i][j] = False
        # print(dp)
        return dp[-1][-1]
