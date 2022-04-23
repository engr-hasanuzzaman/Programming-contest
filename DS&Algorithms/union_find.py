class Solution:
    def find_parent(self, a, par):
        if par[a] == a:
            return a
        return self.find_parent(par[a], par)
    #Function to merge two nodes a and b.
    def union_(self,a,b,par,rank1):
        p_a = self.find_parent(a, par)
        p_b = self.find_parent(b, par)
    
        # alredy connected
        if p_a == p_b:
            return 
        
        r_a, r_b = rank1[p_a], rank1[p_b]
        if r_a > r_b:
            par[p_b] = p_a
            rank1[p_a] += r_b
        else:
            par[p_a] = p_b
            rank1[p_b] += r_a
        
    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        return self.find_parent(x, par) == self.find_parent(y, par)


# keep info 
# idxmap -> value to index mapping to find index with value
# rank wil hold both parten and rank info
# if rank[i] is negetive, that means it is root itself with rankg abs(rank[i])
# _rank() will return rank of given data
# N.B: for numeric value where index indicate node itself, do not need idxmap
class DisJoinSet:
    def __init__(self, elms):
        self.elms = list(elms)
        # value to index
        self.idxmap = {}
        # hold is parent & rank info
        self.rank = []
        for i in range(len(elms)):
            self.idxmap[self.elms[i]] = i
            self.rank.append(-1)

    def parent(self, x):
        # print("---find parent for x", x, self.idxmap, self.rank)
        if self.__rank(x) < 0:
            return x

        val = x
        while self.__rank(val) >= 0:
            val = self.elms[self.__rank(val)]
        
        # path compressiong
        self.rank[self.idxmap[x]] = self.idxmap[val]
        return val

    def __rank(self, x):
        return self.rank[self.idxmap[x]]

    def union(self, u, v):
        p_u, p_v = self.parent(u), self.parent(v)
        if p_u == p_v:
            return

        r_u, r_v = abs(self.__rank(p_u)), abs(self.__rank(p_v))
        if r_u > r_v:
            self.rank[self.idxmap[p_u]] = -(r_u + r_v)
            self.rank[self.idxmap[p_v]] = self.idxmap[p_u]
        else:
            self.rank[self.idxmap[p_v]] = -(r_u + r_v)
            self.rank[self.idxmap[p_u]] = self.idxmap[p_v]

    def is_connected(self, u, v):
        return self.parent(u) == self.parent(v)

# elms
elms = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
ds = DisJoinSet(elms)

ds.union('a', 'b')
ds.union('a', 'f')
ds.union('f', 'g')
ds.union('g', 'b')
# a,b,g,f are connected
ds.union('c', 'l')
ds.union('l', 'i')
ds.union('j', 'i')
ds.union('k', 'c')
assert ds.is_connected('a', 'g') == True
# print(f"---parent of a is {ds.parent('a')}")
# print(f"---parent of b is {ds.parent('b')}")
# print(f"---parent of f is {ds.parent('f')}")
# print(f"---parent of g is {ds.parent('g')}")
assert ds.is_connected('a', 'k') == False

assert ds.is_connected('c', 'i') == True
assert ds.is_connected('c', 'l') == True
# print(ds.parent('c'))
# print(ds.rank[ds.idxmap[ds.parent('c')]])
assert ds.rank[ds.idxmap[ds.parent('c')]] == -5
print(ds.rank[ds.idxmap[ds.parent('a')]])
print(ds.rank[ds.idxmap[ds.parent('k')]])
ds.union('a', 'k')
assert ds.rank[ds.idxmap[ds.parent('c')]] == -9

        