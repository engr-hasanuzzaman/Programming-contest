'''
Algorithm:
- Mark the id of each node un-visit
- Start DFS, upon visitin a node assign id, low_link_value = id, mark in stack, keep in stack
and mark visited
- explore neiboring nodes, after exploring each node, check if the neighboring node in stack
(in stack means, we have cycle that's way we cameback to the currently visiting node)
and update lowlink value of current/parent node (maintain lowlink array)
- after visiting each nodes, check if the current node's low link value is same as id (initial value)
that means this is the starting point of the SSC. Pop all the nodes till current node from statck and
mark those node are not in stack
- all the nodes with same low-link value form a SSC
'''
from collections import defaultdict


class Solution:

    # Function to return a list of lists of integers denoting the members
    # of strongly connected components in the given graph.
    def tarjans(self, V, adj):
        # code here
        self.stack = []
        self.in_stack = defaultdict(bool)
        self.id = [None] * V
        self.weak_link = [None] * V
        self.visited = {}

        # visit the un-visited node
        count = 0
        self.dfs(0, adj)
        for node in range(V):
            if node not in self.visited:
                count += 1
                self.dfs(node, adj)
        groups = defaultdict(list)
        for node, id in enumerate(self.weak_link):
            groups[id].append(node)
 
        # show shorted order
        ans = []
        for a in groups.values():
            a.sort()
            ans.append(a[0:])
        ans.sort()
        return ans

    def dfs(self, node, adj):
        self.id[node] = node
        self.weak_link[node] = node
        self.in_stack[node] = True
        self.stack.append(node)
        self.visited[node] = True

        for neighbor in adj[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor, adj)

            if self.in_stack[neighbor]:
                self.weak_link[node] = min(
                    self.weak_link[node], self.weak_link[neighbor])

        # remove connected component from statck
        if self.weak_link[node] == self.id[node]:
            while True:
                n = self.stack.pop()
                self.in_stack[n] = False
                if n == node:
                    break

sol = Solution()
graph = [[1],[2],[0],[4,7],[5],[6,0],[0, 2, 4],[5,3]]
print("------- ", sol.tarjans(8, graph))
