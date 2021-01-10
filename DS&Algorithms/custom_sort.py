from functools import cmp_to_key

# lets have list of pair, sort by 2nd element
# ex. [(5,6), (2,4), (12, 1)] => [(12, 1), (2,4), (5,6)]

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

data = [Pair(5,6)]
data.append(Pair(2,4))
data.append(Pair(2,4))
data.append(Pair(12,1))

print([(i.a, i.b) for i in sorted(data, key=cmp_to_key(lambda e1, e2: e1.b - e2.b))])