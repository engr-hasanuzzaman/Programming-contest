class Solution:
    def dfsOfGraph(self, V, adj):
        self.visited = [False for _ in range(V)]
        self.ans = []
        self.g = adj
        self.dfs(0)
        return self.ans

    def dfs(self, at):
        if self.visited[at]: 
            return
        self.ans.append(at)
        self.visited[at] = True
        for n in self.g[at]:
            self.dfs(n)