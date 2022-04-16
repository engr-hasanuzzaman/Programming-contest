# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 2
        degree = [0] * n

        # find the degree of nodes
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if degree[u] > 1:
                return u
            if degree[v] > 1:
                return v
