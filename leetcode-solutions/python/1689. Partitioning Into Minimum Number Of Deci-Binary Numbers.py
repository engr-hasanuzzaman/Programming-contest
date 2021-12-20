# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(n[i]) for i in range(len(n))])
