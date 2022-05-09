# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.conversion = defaultdict(dict)
        self.queries = queries
        self.add_to_conversion(equations, values)
        self.visited = defaultdict(bool)
        ans = []
        for node1, node2 in queries:
            if node1 not in self.conversion or node2 not in self.conversion:
                ans.append(-1.00000)
                continue
            # find a -> b value
            val = self.dfs(node1, node2)
            if val:
                ans.append(val)
            else:
                ans.append(-1.00000)
        return ans

    def add_to_conversion(self, equations, values):
        for i in range(len(equations)):
            eq = equations[i]
            value = values[i]
            # a: {b: 2} -> a == 2b
            self.conversion[eq[0]][eq[1]] = value
            self.conversion[eq[1]][eq[0]] = 1 / value

    def dfs(self, node, target):
        if target not in self.conversion:
            return None
        if self.visited[node]:
            return None
        if target in self.conversion[node]:
            return self.conversion[node][target]

        self.visited[node] = True
        ans = None
        for neightbor in self.conversion[node].keys():
            if self.visited[neightbor]:
                continue
            res = self.dfs(neightbor, target)

            if res:
                ans = res * self.conversion[node][neightbor]
                break
        self.visited[node] = False
        return ans
