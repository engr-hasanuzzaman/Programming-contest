from collections import defaultdict


class Solution:

    # Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    visited = defaultdict(bool)
		for node in range(V):
		    if visited[node]:
		        continue
		    if self.hasCycle(node, None, visited):
		        return True
		return False

    def hasCycle(self, node, parent, visited):
        visited[node] = True
        for neighbor in adj[node]:
            if visited[neighbor] and neighbor != parent:
                return True
            
            if not visited[neighbor]:
                resp = self.hasCycle(neighbor, node, visited)
                if resp:
                    return resp
        return False
