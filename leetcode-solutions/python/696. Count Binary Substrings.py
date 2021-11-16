# https://leetcode.com/problems/count-binary-substrings/

# Timelimit exit solution
# take every even size sub-string and check
# we can keep memo for getting help few scenario
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        sub_size = 2
        memo = {}
        while sub_size <= len(s):
            i, j = 0, len(s)
            while i + sub_size <= j:
                if (s[i:i+sub_size] in memo and memo[s[i:i+sub_size]]) or self.valid(s[i:i+sub_size]):
                    count += 1
                    memo[s[i:i+sub_size]] = True
                else:
                    memo[s[i:i+sub_size]] = False
                i += 1
            sub_size = sub_size + 2
        return count

    def valid(self, s: str) -> bool:
        f_char = s[0]
        l_char = s[-1]
        if f_char == l_char:
            return False

        for i in range(len(s)//2):
            if s[i] != f_char:
                return False

        for i in range(len(s)//2, len(s)):
            if s[i] != l_char:
                return False

        return True

# accepted solution
'''
Let's try to count the number of valid binary strings between groups[i] and groups[i+1].
If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000".
We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string.
Because the binary digits to the left or right of this string must change at the boundary,
our answer can never be larger.
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = []
        last_char = s[0]
        count = 0
        for i in range(len(s)):
            if s[i] == last_char:
                count += 1
            else:
                group.append(count)
                last_char = s[i]
                count = 1
        # insert the last char count
        group.append(count)
        ans = 0
        # ex: 000111 -> 0011 -> 01 so min size of the two char count
        for i in range(len(group) - 1):
            ans = ans + min(group[i], group[i+1])
        return ans
