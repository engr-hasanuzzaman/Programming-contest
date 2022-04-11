# Strongly Connected Components (Kosaraju's Algo) 

# use dfs to find the reverse postorder on Reversed Graph/Original Graph
# use the post order vertix to run dfs/bfs on Original/Reversed graph to mark strongly connected elements
from collections import defaultdict

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        stack = []
        visited = defaultdict(lambda: False)
        reverse_graph = self.reverse_graph(adj)
        for i in range(V):
            if not visited[i]:
                self.dfs_reverse_postorder(reverse_graph, i, stack, visited)
        
        visited.clear()
        ids = {}
        number = 0
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                number += 1
                self.dfs_marking(adj, vertex, number, ids, visited)
        return number

    def reverse_graph(self, adj):
        rev_adj = [[] for _ in range(len(adj))]
        for i, neighbors in enumerate(adj):
            for n in neighbors:
                rev_adj[n].append(i)
    
        return rev_adj
        
    def dfs_reverse_postorder(self, graph, node, stack, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited.get(neighbor, False):
                self.dfs_reverse_postorder(graph, neighbor, stack, visited)
        stack.append(node)
    
    def dfs_marking(self, graph, v, number, ids, visited):
        ids[number] = True
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                self.dfs_marking(graph, neighbor, number, ids, visited)
