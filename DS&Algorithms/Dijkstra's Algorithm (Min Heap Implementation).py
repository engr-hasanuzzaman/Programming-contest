from heapq import *
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [float('inf') for _ in range(V)]
        dist[S] = 0
        heap = []
        heappush(heap, (0, S))
        
        while heap:
            w, cur = heappop(heap)
            for neighbor, weight in adj[cur]:
                if dist[neighbor] > w + weight:
                    # w + weight -> dist[cur] + weight
                    heappush(heap, (dist[cur] + weight, neighbor))
                    dist[neighbor] = w + weight
        return dist