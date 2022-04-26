#User function Template for python3

class Solution:
    def helpaterp(self, hospital):
        R = len(hospital)
        if R == 0: return -1
        C = len(hospital[0])
        queue = []
        uninfected_patient_count = 0
        for i in range(R):
            for j in range(C):
                if hospital[i][j] == 2:
                    queue.append((i, j))
                if hospital[i][j] == 1:
                    uninfected_patient_count += 1
        count = -1
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            l_size = len(queue)
            temp = []
            count += 1
            # print("----current size ", l_size)
            for _ in range(l_size):
                r, c = queue.pop()
                for rr, cc in neighbors:
                    n_row = r + rr
                    n_col = c + cc
                    if n_row < 0 or n_row >= R or n_col < 0 or n_col >= C:
                        continue
                    if hospital[n_row][n_col] != 1:
                        continue
                    # infected
                    uninfected_patient_count -= 1
                    hospital[n_row][n_col] = 2
                    temp.append((n_row, n_col))
            queue = temp
        if uninfected_patient_count > 0:
            return -1
        else:
            return count
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        
        rc=input().split() #row and column
        r=int(rc[0])    
        c=int(rc[1])
        
        
        hospital=[]
        
        for i in range(r):
            hospital.append([int(j) for j in input().split()])
            
        ob = Solution()        
        print(ob.helpaterp(hospital))

# } Driver Code Ends