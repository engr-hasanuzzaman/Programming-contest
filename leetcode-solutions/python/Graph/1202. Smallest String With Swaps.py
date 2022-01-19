# https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ds = DisjoinSet(len(s))
        for [i, j] in pairs:
            ds.union(i, j)
        component = defaultdict(list)
        for i in range(len(s)):
            component[ds.find(i)].append(s[i])
            
        for key in component:
            component[key].sort(reverse=True)
        
        return "".join([component[ds.find(i)].pop() for i in range(len(s))])
        
class DisjoinSet():
    def __init__(self, n):
        self.edges = [-1 for _ in range(n)]
    
    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 != p2:
            if abs(self.edges[p1]) >= abs(self.edges[p1]):
                self.edges[p1] += self.edges[p2]
                self.edges[p2] = p1
            else:
                self.edges[p2] += self.edges[p1]
                self.edges[p1] = p2
    
    def find(self, edge):
        cur_edge = edge
        while self.edges[cur_edge] >= 0:
            cur_edge = self.edges[cur_edge]
        
        if edge != cur_edge:
            self.edges[edge] = cur_edge
        return cur_edge
