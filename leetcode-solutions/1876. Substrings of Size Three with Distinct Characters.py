# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if self.uniq(s[i:i+3]):
                count += 1
        return count
            
    def uniq(self, s):
        memo = {}
        for _, char in enumerate(s):
            if char in memo:
                return False
            
            memo[char] = True
        return True


# generic solution which will work for any size 
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        count = 0
        memo = defaultdict(int)
        uniq_count = 0
        size = 3

        # keep size number of char in memo
        for i in range(size):
            if s[i] in memo:
                memo[s[i]] += 1
                uniq_count -= 1
            else:
                memo[s[i]] = 1
                uniq_count += 1

        # start from size to end
        for i in range(size, len(s)):
            # update the count if uniq_count is size
            if uniq_count == size:
                count += 1

            # remove last char to maintain the size
            # if count was 1 then decrease uniq_count
            # elsif count was 2 then increase (for > 2 do not need to chage uniq_count)
            if memo[s[i-size]] == 1:
                uniq_count -= 1
            elif memo[s[i-size]] == 2:
                uniq_count += 1
            memo[s[i-size]] -= 1

            # upate current char count
            if s[i] in memo:
                memo[s[i]] += 1
            else:
                memo[s[i]] = 1

            # if new count 1 increase uniq_count
            # if new count 2 decrease uniq_count
            if memo[s[i]] == 1:
                 uniq_count += 1
            elif memo[s[i]] ==  2:
                uniq_count -= 1
        # after processing the last char if still uniq_count is = to size
        if uniq_count == size:
            count += 1
        return count
