# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur_list = []
        self.dfs(0, ans, cur_list, s)
        return ans
    def dfs(self, start, result, cur_list, s):
        if start >= len(s):
            result.append([i for i in cur_list])
            return
        end = start
        while end < len(s):
            if self.is_palindrom(s, start, end):
                cur_list.append(s[start:end+1])
                self.dfs(end + 1, result, cur_list, s)
                cur_list.pop()
            end += 1
            
    def is_palindrom(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
