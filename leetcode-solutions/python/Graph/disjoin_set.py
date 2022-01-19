# find fast implementation
from mimetypes import init
import unittest


class DisJoin():
    def __init__(self, size) -> None:
        self.edges = []
        for i in range(size):
            self.edges.append(i)
        
    def find(self, node) -> int:
        return self.edges[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            for i in range(len(self.edges)):
                if self.edges[i] == root2:
                    self.edges[i] = root1
    def connected(self, edge1, edge2):
        return self.edges[edge1] == self.edges[edge2]

# testing section
ds = DisJoin(9)
ds.union(0, 1)
ds.union(0, 2)
ds.union(2, 3)
ds.union(4, 2)

ds.union(5, 6)
ds.union(5, 7)

assert ds.connected(0, 4) == True
assert ds.connected(0, 5) == False
assert ds.connected(7, 5) == True
assert ds.connected(7, 8) == False

# 2nd set test
uf = DisJoin(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.connected(1, 5) == True
assert uf.connected(5, 7) == True
assert uf.connected(4, 9) == False
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
assert uf.connected(4, 9) == True
print(uf.edges)

# quick union
class QuickUnionDisjoin():
    def __init__(self, size) -> None:
        self.edges = [e for e in range(size)]

    # find the root of passing edge
    # worse case time complexity is O(N)
    def find(self, edge):
        while edge != self.edges[edge]:
            edge = self.edges[edge]
        return edge
    
    # worse case scenirio is O(N) as we are using find method which has O(N) time complexity
    def union(self, e1, e2):
        root1 = self.find(e1)
        root2 = self.find(e2)
        if root1 != root2:
            self.edges[root1] = root2

    def connected(self, e1, e2):
        return self.find(e1) == self.find(e2)
    
uf = QuickUnionDisjoin(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.connected(1, 5) == True
assert uf.connected(5, 7) == True
assert uf.connected(4, 9) == False
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
assert uf.connected(4, 9) == True
print(uf.edges)

ds = QuickUnionDisjoin(9)
ds.union(0, 1)
ds.union(0, 2)
ds.union(2, 3)
ds.union(4, 2)

ds.union(5, 6)
ds.union(5, 7)

assert ds.connected(0, 4) == True
assert ds.connected(0, 5) == False
assert ds.connected(7, 5) == True
assert ds.connected(7, 8) == False
print(ds.edges)

class DisjoinRank():
    def __init__(self, n) -> None:
        self.edges = [-1 for _ in range(n)]

    def find(self, edge):
        cur_edge = edge
        while self.edges[cur_edge] >= 0:
            cur_edge = self.edges[cur_edge]
        
        # compression
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

# testing section
ds = DisjoinRank(9)
ds.union(0, 1)
ds.union(0, 2)
ds.union(2, 3)
ds.union(4, 2)

ds.union(5, 6)
ds.union(5, 7)

assert ds.connected(0, 4) == True
assert ds.connected(0, 5) == False
assert ds.connected(7, 5) == True
assert ds.connected(7, 8) == False

uf = DisjoinRank(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.connected(1, 5) == True
assert uf.connected(5, 7) == True
assert uf.connected(4, 9) == False
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
assert uf.connected(4, 9) == True
print(uf.edges)