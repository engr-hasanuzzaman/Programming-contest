# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.combination(ans, 1, k, n+1, [])
        return ans

    def combination(self, ans, start, k, n, cur_list):
        if start + k > n:
            return

        if k == 0:
            ans.append(cur_list[:])

        for i in range(start, n):
            cur_list.append(i)
            self.combination(ans, i+1, k-1, n, cur_list)
            cur_list.pop()
