# https://leetcode.com/problems/permutation-in-string/

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frequency = Counter(s1)

        i = start = 0
        cur_size = 0
        cur_frequency = frequency.copy()
        while i < len(s2):
            char = s2[i]
            if char in cur_frequency and cur_frequency[char] > 0:
                cur_size += 1
                cur_frequency[char] -= 1
                if cur_size == len(s1):
                    return True
            # value is zero
            elif char in cur_frequency:
                # remove char from start untill cur_frequency[char] > 0 which might be our potential solution
                while cur_frequency[char] == 0:
                    # print(start)
                    cur_frequency[s2[start]] += 1
                    cur_size -= 1
                    start += 1
                # now consider the current char
                cur_size += 1
                cur_frequency[char] -= 1
            else:
                cur_size = 0
                start = i + 1
                cur_frequency = frequency.copy()
            i += 1
        return False
