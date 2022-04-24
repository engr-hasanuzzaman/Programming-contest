class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        dist = [100000000 for _ in range(V)]
        dist[S] = 0
        for _ in range(V-1):
            for u, v, w in adj:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist
