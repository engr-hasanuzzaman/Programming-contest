# https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        # we have two possible patters 101 or 010
        # for 101 if we know number of 1 before & after 0 (m, n) result will be m * n
        # same for 010

        one = zero = 0
        # for 0, it will contain number of 1
        # for 1, it will contain number of 0
        before = []
        for char in s:
            if char == '0':
                zero += 1
                before.append(one)
            else:
                one += 1
                before.append(zero)
        
        # calculat how many 1 exist after 0 and how many 0 after 1
        one = zero = 0
        after = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                zero += 1
                after.append(one)
            else:
                one += 1
                after.append(zero)
        
        #since we have keept after in reverse order last one first, rev it
        after = after[::-1]
        count = 0
        for i in range(len(s)):
            count += after[i] * before[i]
        return count
        