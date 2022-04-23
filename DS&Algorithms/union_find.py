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
