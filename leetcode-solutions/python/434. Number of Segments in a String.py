# https://leetcode.com/problems/number-of-segments-in-a-string/
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
