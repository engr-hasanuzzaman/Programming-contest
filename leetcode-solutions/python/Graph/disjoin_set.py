# find fast implementation
import unittest


class DisJoin():
    def __init__(self, size) -> None:
        self.edges = []
        for i in range(size):
            self.edges.append(i)
        
    def find(self, node) -> int:
        return self.edges[node]

    def join(self, node1, node2):
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
ds.join(0, 1)
ds.join(0, 2)
ds.join(2, 3)
ds.join(4, 2)

ds.join(5, 6)
ds.join(5, 7)

assert ds.connected(0, 4) == True
assert ds.connected(0, 5) == False
assert ds.connected(7, 5) == True
assert ds.connected(7, 8) == False
