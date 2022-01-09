# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        anagram = {}
        for _, c in enumerate(s1):
            if c in anagram:
                anagram[c] += 1
            else:
                anagram[c] = 1
        i = start = 0
        cur_size = 0
        cur_anagram = anagram.copy()
        while i < len(s2):
            char = s2[i]
            if char in cur_anagram and cur_anagram[char] > 0:
                cur_size += 1
                cur_anagram[char] -= 1
                if cur_size == len(s1):
                    return True
            # value is zero             
            elif char in cur_anagram:
                # remove char from start untill cur_anagram[char] > 0 which might be our potential solution
                while cur_anagram[char] == 0:
                    # print(start)
                    cur_anagram[s2[start]] += 1
                    cur_size -= 1
                    start += 1
                # now consider the current char
                cur_size += 1
                cur_anagram[char] -= 1
            else:
                cur_size = 0
                start = i + 1
                cur_anagram = anagram.copy()
            i += 1
        return False
