# use fenwick tree
class PrefixSum2d:
    def __init__(self, data, row_size, col_size):
        self.bit = [[0] * (col_size +1) for _ in range(row_size+1)]
        self.data = data
        self.row_size = row_size
        self.col_size = col_size
        for i in range(1, self.row_size+1):
            for j in range(1, self.col_size+1):
                self._add(i, j, data[i-1][j-1])
    
    def _add(self, i, j, val):
        while i <= self.row_size:
            while j <= self.col_size:
                self.bit[i][j] += val
                j += (j & -j)
            i += (i & -i)
    def sum(self, x, y):
        res = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res

data = [[ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ], 
     [ 1, 1, 1, 1, 1 ]] 
p = PrefixSum2d(data, len(data), len(data[0]))
# print(p.bit)
print(p.sum(4, 3))