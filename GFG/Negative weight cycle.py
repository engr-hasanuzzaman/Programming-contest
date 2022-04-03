# https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1#

# User function Template for python3

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        distance = [float('inf') for _ in range(n)]
        # consider first note as source node
        distance[0] = 0
        has_negetive_cycle = 0

        for i in range(n-1):
            for u, v, w in edges:
                distance[v] = min(distance[v], distance[u] + w)

        # check negetive cycle
        for u, v, w in edges:
            if distance[v] > distance[u] + w:
                has_negetive_cycle = 1
                break

        return has_negetive_cycle
