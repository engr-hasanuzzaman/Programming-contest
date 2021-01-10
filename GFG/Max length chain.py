from functools import cmp_to_key

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(Parr, n):
    Parr = sorted(Parr, key=cmp_to_key(lambda e1, e2: e1.b - e2.b))
    max_pair = 1
    for i in range(0, len(Parr)):
        cur_pair = 1
        cur_val = Parr[i]
        for j in range(i+1, len(Parr)):
            if cur_val.b < Parr[j].a:
                cur_pair += 1
                cur_val = Parr[j]
        if cur_pair > max_pair:
            max_pair = cur_pair
    return max_pair