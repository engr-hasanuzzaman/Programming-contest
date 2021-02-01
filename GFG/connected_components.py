# given an undirected graph as adjacency list, find the strongly connected component
class Solution:
    # g is graph as adjacency list
    # n number of vertix(node)
    def connected_components(self, g, n):
        self.g = g
        self.visited = [False for _ in range(n)]
        self.components = [0 for _ in range(n)]
        self.count = 0
        for at in range(n):
            if self.visited[at]:
                continue
            self.dfs(at)
            self.count += 1
        return self.components
    
    def dfs(self, at):
        if self.visited[at]:
            return
        
        self.visited[at] = True
        self.components[at] = self.count
        for n in self.g[at]:
            self.dfs(n)

graph = [[1,2], [0,2], [1], [4], [3]]
obj = Solution()
obj.connected_components(graph, 5)
print(obj.components)