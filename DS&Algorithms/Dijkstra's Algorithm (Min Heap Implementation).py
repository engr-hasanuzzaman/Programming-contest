from heapq import *
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        # from start, set min cost is inf
        min_cost = [float('inf') for _ in range(V)]
        # for the starting vertex cost is 0 (from 0 to 0)
        min_cost[S] = 0
        # since 0 min value start with 0 edge
        heap = [S]
        while heap:
            # using heap to get min value
            node = heappop(heap)
            elapsed_cost = min_cost[node]
            # update all the neighbors with updated cost
            for neighbor, cost in adj[node]:
                # if new cost is smaller, update and put on stack to update all the corresponding
                # neighbors
                if elapsed_cost + cost < min_cost[neighbor]:
                    min_cost[neighbor] = elapsed_cost + cost
                    heappush(heap, neighbor)
        return min_cost