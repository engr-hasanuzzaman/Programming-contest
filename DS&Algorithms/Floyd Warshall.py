# need to prepare n * b matrix representation of the graph
# create n * n dp & next (if not want to change input)
# for exiting weight add dp[i][j] = graph[i][j] and next[i][j] = j if there is a path between i & j
# update dp
# for i & j, if dp[i][k] + dp[k][j] < dp[i][j] update dp[i][j] & next[i][j] = next[i][k]
# dp[i][j] = 

# the theme of the algorithm is, 
# if we use every node as the intermediatory nodes between two nodes, does it give us min val?
class Solution:
    def shortest_distance(self, dp):
        size = len(dp)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                i_k = float('inf') if dp[i][k] == -1 else dp[i][k]
                i_j = float('inf') if dp[i][j] == -1 else dp[i][j]
                k_j = float('inf') if dp[k][j] == -1 else dp[k][j]
                val = min(i_j, i_k + k_j)
                if val == float('inf'):
                    continue
                # print("i {i}, j {j}, k {k}", i, j, k, min(dp[i][k] + dp[k][j], dp[i][j]))
                dp[i][j] = val

