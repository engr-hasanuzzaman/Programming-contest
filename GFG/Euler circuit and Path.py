# if every vertex has even degree, it has Euclidian circuit, 
# if has two odd degree, it has Eculidian path
class Solution:
    def isEularCircuitExist(self, V, adj):
        odd_degree = 0
        for neighbors in adj:
            if len(neighbors) % 2 != 0:
                odd_degree += 1

        if odd_degree == 0:
            return 2
        elif odd_degree == 2:
            return 1
        else:
            return 0
