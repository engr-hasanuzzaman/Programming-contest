# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for [i, j] in edges:
            graph[i].append(j)
            graph[j].append(i)

        stack = [source]
        visited = [False] * n
        visited[source] = True
        while stack:
            current = stack.pop()
            if current == destination:
                return True
            for neighbor in graph[current]:
                # return early
                if neighbor == destination:
                    return True
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
        return False