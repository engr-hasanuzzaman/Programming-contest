# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ds = DisjoinSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    ds.union(i, j)
        count = 0
        for p in ds.edges:
            # if the root edge
            if p < 0:
                count += 1
        return count
    
class DisjoinSet():
    def __init__(self, n):
        # have negetive value means it is root node
        self.edges = [-1 for _ in range(n)]
    
    def find(self, edge):
        cur_edge = edge
        while self.edges[cur_edge] >= 0:
            cur_edge = self.edges[cur_edge]
        
        if edge != cur_edge:
            self.edges[edge] = cur_edge

        return cur_edge
    
    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 != p2:
            if abs(self.edges[p1]) >= abs(self.edges[p2]):
                self.edges[p1] += self.edges[p2]
                self.edges[p2] = p1
            else:
                self.edges[p2] += self.edges[p1]
                self.edges[p1] = p2
    
    def connected(self, e1, e2):
        return self.find(e1) == self.find(e2)