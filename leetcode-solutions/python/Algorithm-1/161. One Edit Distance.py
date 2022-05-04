# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        if len(s) == len(t):
            return self.isOneEditDistanceWithReplace(s, t)
        else:
            return self.isOneEditDistanceWithAddOrRemote(s, t)

    def isOneEditDistanceWithReplace(self, s, t):
        idx = 0
        diff_count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff_count += 1

            if diff_count > 1:
                return False
        return True

    # assume len(s) > len(t)
    def isOneEditDistanceWithAddOrRemote(self, s, t):
        if len(t) > len(s):
            return self.isOneEditDistanceWithAddOrRemote(t, s)

        idx_s = idx_t = 0
        while idx_s < len(s) and idx_t < len(t) and s[idx_s] == t[idx_t]:
            idx_s += 1
            idx_t += 1

        return s[idx_s+1:] == t[idx_t:]
