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
                if self.edges[i] == root1:
                    self.edges[root2] = root1

# testing section
ds = DisJoin(9)
ds.join(0, 1)
ds.join(0, 2)
ds.join(2, 3)
ds.join(4, 2)

ds.join(5, 6)
ds.join(5, 7)

# assert ds.find(3) == ds.find(0)
print(ds.find(4), ds.find(0))
print(ds.edges)
