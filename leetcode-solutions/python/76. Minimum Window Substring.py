# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N, M = len(s), len(t)
        if M > N:
            return ""
        
        char_count = defaultdict(int)
        for _, char in enumerate(t):
            char_count[char] += 1
        
        start = 0
        char_found = 0
        char_char_count = defaultdict(int)
        ans = s
        solution_found = False
        for i, char in enumerate(s):
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    char_found += 1
                # print(char_found, len(t))
                if char_found == len(char_count):
                    solution_found = True
                    # shint the string
                    while char_found == len(char_count):
                        # update sub-string
                        if len(ans) > (i - start + 1):
                            ans = s[start:i+1]
                         
                        if s[start] in char_count:
                            char_count[s[start]] += 1
                            if char_count[s[start]] > 0:
                                char_found -= 1
                            
                        start += 1
        if not solution_found:
            return ""
        return ans
    