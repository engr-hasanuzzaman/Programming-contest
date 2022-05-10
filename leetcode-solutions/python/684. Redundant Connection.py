# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_of_nodes = len(edges) + 1
        disjoin_set = DisjointSet(num_of_nodes)
        ans = []
        for node1, node2 in edges:
            if disjoin_set.is_connected(node1, node2):
                ans = [node1, node2]
                continue
            disjoin_set.union(node1, node2)

        return ans


class DisjointSet:
    def __init__(self, size):
        self.nodes = [-1] * size

    def find(self, node):
        # negtive val means root
        if self.nodes[node] < 0:
            return node

        return self.find(self.nodes[node])

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 == p2:
            return
        parent1_weight = abs(self.nodes[p1])
        parent2_weight = abs(self.nodes[p2])

        # ensure p1 > p2
        if parent2_weight > parent1_weight:
            parent1_weight, parent2_weight = parent2_weight, parent1_weight
            p1, p2 = p2, p1

        self.nodes[p2] = p1
        self.nodes[p1] = -(parent1_weight + parent2_weight)

    def is_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
