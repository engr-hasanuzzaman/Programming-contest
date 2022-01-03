# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, int(n)
        while s < e:
            mid = (e - s) // 2 + s
            r = isBadVersion(mid)
            if r:
                e = mid
            else:
                s = mid + 1
        # print(s)
        return s
