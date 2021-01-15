class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        table = [[0]*len(S2) for _ in range(len(S1))]
        max_length = 0
        for i in range(len(S1)):
            for j in range(len(S2)):
                if i == 0 or j == 0:
                    if S1[i] == S2[j]:
                        table[i][j] = 1
                        max_length = max(1, max_length)
                else:
                    if S1[i] == S2[j]:
                        table[i][j] = table[i-1][j-1] + 1
                        max_length = max(table[i][j], max_length)
                    else:
                        table[i][j] = 0
        return max_length
