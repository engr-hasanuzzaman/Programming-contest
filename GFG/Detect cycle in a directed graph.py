from collections import defaultdict

# TLE solution


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # print(adj)
        self.visited = defaultdict(bool)
        self.overall_visit = defaultdict(bool)
        self.has_cycle = False
        for node in range(V):
            if self.overall_visit[node]:
                continue
            self.dfs(adj, node)
            if self.has_cycle:
                break
        return self.has_cycle

    def dfs(self, adj, node):
        self.overall_visit[node] = True
        if self.visited[node] or self.has_cycle:
            # print(self.visited, node)
            self.has_cycle = True
            return
        self.visited[node] = True

        for neighbor in adj[node]:
            self.dfs(adj, neighbor)
        self.visited[node] = False


# Accepted solution


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # print(adj)
        self.visiting = defaultdict(bool)
        self.overall_visit = defaultdict(bool)
        self.has_cycle = False
        for node in range(V):
            if self.overall_visit[node]:
                continue
            self.dfs(adj, node)
            if self.has_cycle:
                break
        return self.has_cycle

    def dfs(self, adj, node):
        self.visiting[node] = True
        for neighbor in adj[node]:
            if self.visiting[neighbor]:
                self.has_cycle = True
                return True

            if not self.overall_visit[neighbor]:
                self.dfs(adj, neighbor)
        self.visiting[node] = False
        self.overall_visit[node] = True
