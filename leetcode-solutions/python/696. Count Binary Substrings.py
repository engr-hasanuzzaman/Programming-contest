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
